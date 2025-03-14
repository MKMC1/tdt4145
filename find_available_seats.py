import sqlite3

conn = sqlite3.connect('prosjekt.db')
print("Connection Successful")

def get_available_flights(conn):
    # Henter tilgjengelige flyvninger med lopeNr og flytypeNavn
    cursor = conn.cursor()
    cursor.execute('''
        SELECT DISTINCT Flyvning.flightNr, Flyvning.dato, Flyvning.lopeNr, Fly.flytypeNavn
        FROM Flyvning
        JOIN Fly ON Flyvning.registreringsNr = Fly.registreringsNr
        ORDER BY Flyvning.flightNr ASC
    ''')
    return cursor.fetchall()

def get_seat_configuration(conn, flytypeNavn):
    # Henter setekonfigurasjonen fra databasen
    cursor = conn.cursor()
    cursor.execute('''
        SELECT seterPerRad, rader, seteMarkering, radNodutgang
        FROM konfigurasjon
        WHERE flytypeNavn = ?
    ''', (flytypeNavn,))
    row = cursor.fetchone()
    if row:
        seterPerRad, rader, seteMarkering, radNodutgang = row
        nødutganger = [int(r) for r in str(radNodutgang).split('-')] if radNodutgang else []
        return seterPerRad, rader, seteMarkering, nødutganger
    return None

def generate_seats(conn, flytypeNavn):
    # Genererer alle seter basert på setekonfigurasjonen
    seat_config = get_seat_configuration(conn, flytypeNavn)
    if not seat_config:
        return []
    
    seterPerRad, rader, seteMarkering, nødutganger = seat_config
    all_seats = []
    
    for rad in range(1, rader + 1):
        if flytypeNavn == "Dash-8 100":
            sete_liste = list("   CD") if rad == 1 else list("AB CD")
        else:
            sete_liste = list(seteMarkering)
        
        for sete in sete_liste:
            all_seats.append((rad, sete, "EXIT" if rad in nødutganger else ""))
    
    return all_seats

def get_sold_seats(conn, lopeNr, flightNr):
    # Henter seter som er solgt for en gitt flyvning basert på lopeNr og flightNr
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.radNr, s.seteBokstav
        FROM Flybillett b
        JOIN Sete s ON b.lopeNr = s.lopeNr AND b.flightNr = s.flightNr
        WHERE b.lopeNr = ? AND b.flightNr = ?
    ''', (lopeNr, flightNr))
    return set(cursor.fetchall())

def display_seats(all_seats, sold_seats, flytypeNavn):
    # Viser setene i en flylayout-stil med midtgang
    seats_by_row = {}
    for row, seat, exit_label in all_seats:
        if row not in seats_by_row:
            seats_by_row[row] = []
        seat_label = "X" if (row, seat) in sold_seats else seat
        seats_by_row[row].append(seat_label)
    
    print("\n" + "="*30)
    print("        Available Seats")
    print("="*30 + "\n")
    
    for row in sorted(seats_by_row.keys()):
        if flytypeNavn == "Dash-8 100":
            left_side = " ".join(seats_by_row[row][:2])
            right_side = " ".join(seats_by_row[row][2:])
        else:
            left_side = " ".join(seats_by_row[row][:3])
            right_side = " ".join(seats_by_row[row][3:])
        exit_label = " (EXIT)" if any("EXIT" in s for s in all_seats if s[0] == row) else ""
        print(f"Row {row:2}:  {left_side}   {right_side}{exit_label}")
    
    print("\nStatus: X = Booked | Available = Shown | (EXIT) = Emergency Exit")
    print("="*30 + "\n")

def main():
    print("Available Flights:")
    flights = get_available_flights(conn)
    
    if not flights:
        print("No flights found. Please check your database.")
        return
    
    for i, flight in enumerate(flights):
        print(f"{i + 1}. Flight: {flight[0]} | Date: {flight[1]} | lopeNr: {flight[2]} | Type: {flight[3]}")
    
    choice = int(input("Select a flight (enter number): ")) - 1
    if 0 <= choice < len(flights):
        selected_flight = flights[choice]
        flightNr = selected_flight[0]
        lopeNr = selected_flight[2]
        flytypeNavn = selected_flight[3]
        
        print(f"\nChecking available seats for Flight {selected_flight[0]} on {selected_flight[1]}...\n")
        
        all_seats = generate_seats(conn, flytypeNavn)
        if not all_seats:
            print("No seat configuration found for this aircraft type.")
            return
        
        sold_seats = get_sold_seats(conn, lopeNr, flightNr)
        display_seats(all_seats, sold_seats, flytypeNavn)
    else:
        print("Invalid selection. Please enter a valid number.")
    
    conn.close()

if __name__ == "__main__":
    main()
