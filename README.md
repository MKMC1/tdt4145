# Bruksanvisning

## Brukstilfelle 1, 2, 3, 4, og 7 
1. Åpne sqlite3 i cmd eller Bash.
2. Bruk .open prosjekt.db for å åpne en tom db-fil, men som har ønsket skjema for databasen.
3. Bruk .read sql_insert_data.sql for å sette inn all dataen.

Databasen er da klar til bruk med alle dataene i vedleggene. 
## Brukstilfelle 5
Her er ren sql-spørring som er for brukstilfelle 5.
```sql
SELECT flyselskap.navn AS Flyselskap, flytypeNavn AS Flytype, Count(flytypeNavn) AS 'Antall fly' FROM Fly
INNER JOIN flyselskap ON fly.flyselskapsKode = flyselskap.flyselskapsKode
GROUP BY flytypeNavn;
```

## Brukstilfelle 6
Skriv commando 
```py
py finn_flyrute.py
```
Brukeren skriver inn valgt flyplasskode, ukedagskode, og om hen vil se avganger eller ankomster. Deretter dukker det opp en tabell hvor brukeren kan se flyrutenummer, planlagt avgangstid eller planlagt ankomsttid avhengig av hva brukeren har valgt, samt alle avganger og ankomster  

## Brukstilfelle 8
Skriv commando 
```py
py finn_ledige_seter.py
```
For å sjekke om hvilken flyvning som har status 'Planned'. Brukeren skal deretter velge hvilket fly som hen ønsker å finne ledige seter for ved å skrive in nummer som flyet tilhører.
Sete som er tatt blir markert med 'X', mens alle andre setene er vist som normalt. 
