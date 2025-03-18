import sqlite3
from collections import defaultdict

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
    reise = "avreise" if flyvning_type == "AVR" else "ankomst"
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
        conn.close() #Lukk tilkoblingen!
        return

    print(f'\nFlyruter funnet for "{reise}" på {flyplass_kode} flyplass, ukedag {ukedag}:\n')

    flyruter = defaultdict(list)

    for rute in ruter:
        flightNr, tid, avreise, ankomst = rute
        flyruter[flightNr].append((tid, avreise, ankomst))

    for flightNr, stopp in flyruter.items():
        print(f"\nFlightNr: {flightNr}")

        stopp.sort()

        rute_rekkefølge = " ➝ ".join([s[1] for s in stopp] + [stopp[-1][2]])

        print(f"   Planlagt {reise} tidspunkt: {stopp[0][0]}")
        print(f"   Rute: {rute_rekkefølge}")
        print("-" * 50)

    conn.close()  #Lukk tilkoblingen!

# Kjøre programmet
finn_flyruter()