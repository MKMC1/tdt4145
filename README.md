# Bruksanvisning

## Brukstilfelle 1, 2, 3, 4, og 7 
Først vær sikker på at du er i samme mappe som alle filene du har lastet ned.

1. Åpne sqlite3 i cmd eller Bash.
   ```
   sqlite3
   ```
3. Bruk .open prosjekt.db for å åpne en tom db-fil, men som har ønsket skjema for databasen.
   ```
   .open prosjekt.db
   ```
5. Bruk .read sql_insert_data.sql for å sette inn all dataen.
   ```
   .read sql_insert_data.sql
   ```

Databasen er da klar til bruk med alle dataene i vedleggene. 
## Brukstilfelle 5
Her er ren sql-spørring som er for brukstilfelle 5, men først skriv denne kommandoen for å få finere utskrift fra sql.
```sql
.mode table
```
Også kan du skrive denne kommandoen:
```sql
SELECT flyselskap.navn AS Flyselskap, flytypeNavn AS Flytype, Count(flytypeNavn) AS 'Antall fly'
FROM Fly INNER JOIN flyselskap ON fly.flyselskapsKode = flyselskap.flyselskapsKode
GROUP BY flytypeNavn;
```
For neste tilfelle må du ut av sqlite3 programmet. Dette gjøres ved å skrive kommandoen:
```py
.exit
```
## Brukstilfelle 6
Skriv kommandoen: 
```py
py finn_flyrute.py
```
Brukeren skriver inn valgt flyplasskode, ukedagskode, og om hen vil se avganger eller ankomster. Deretter dukker det opp en oversikt hvor brukeren kan se alle de aktuelle flyrutenummerne, med planlagt avgangstid eller planlagt ankomsttid avhengig av hva brukeren har valgt, samt hele flyruten. 

## Brukstilfelle 8
Skriv commando 
```py
py finn_ledige_seter.py
```
For å sjekke om hvilken flyvning som har status 'Planned'. Brukeren skal deretter velge hvilket fly som hen ønsker å finne ledige seter for ved å skrive in nummer som flyet tilhører.
Sete som er tatt blir markert med 'X', mens alle andre setene er vist som normalt. 
