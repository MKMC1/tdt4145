import sqlite3


def finn_flyruter():
    """Lar brukeren søke etter flyruter basert på flyplasskode, ukedag og type flyvning (Avgang/Ankomst)."""

    conn = sqlite3.connect("prosjekt.db")  # Koble til SQLite database
    print("Connection successful!")

    cursor = conn.cursor()  # Lag et cursor objekt

    # Brukerinput
    flyplass_kode = input("Skriv inn flyplasskode (f.eks. TRD, OSL, BOO): ").upper()
    ukedag = input("Skriv inn ukedag (1 = Mandag, ..., 7 = Søndag): ")

    # Valider brukerinput
    while True:
        flyvning_type = input("Skriv 'Avr' for avreise eller 'Ank' for ankomster: ").upper()
        if flyvning_type in ["AVR", "ANK"]:
            break  
        print("Ugyldig valg! Skriv 'Avr' for avreise eller 'Ank' for ankomster.")

    tidskolonne = "planlagtAvreistTid" if flyvning_type == "AVR" else "planlagtAnkomstTid"
    reisekolonne = "avreiseFlyplassKode" if flyvning_type == "AVR" else "ankomstFlyplassKode"
    # SQL-spørring basert på flyvning_type
    sql = f"""
    SELECT Delreise.flightNr, Delreise.{tidskolonne}, avreiseFlyplassKode, ankomstFlyplassKode
    FROM Delreise
    JOIN Flyruter ON Flyruter.flightNr = Delreise.flightNr
    WHERE Delreise.flightNr IN (
        SELECT DISTINCT flightNr
        FROM Delreise
        WHERE {reisekolonne} = ?
        AND ukedagsKode LIKE '%' || ? || '%'
    )
    ORDER BY Delreise.flightNr, Delreise.{tidskolonne};
    """

    # Utfør SQL-spørringen
    cursor.execute(sql, (flyplass_kode, str(ukedag)))
    ruter = cursor.fetchall()

    # Skriv ut resultatene
    if not ruter:
        print("Ingen flyruter funnet for denne flyplassen og ukedagen.")
    else:
        print("\nFlyruter funnet:\n")
        print(
            f"{'flightNr':<10} {tidskolonne:<20} {'avreise':<7} {'ankomst':<7}"
        )
        print("-" * 65)

    for rute in ruter:
        print(
            f"{rute[0]:<10} {rute[1]:<20} {rute[2]:<7} {rute[3]:<7}"
        )

    conn.close()  # Close the connection


# Kjør programmet
finn_flyruter()
