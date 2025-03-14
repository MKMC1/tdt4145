# Bruksanvisning

1. Åpne sqlite3 i cmd eller Bash.
2. Bruk .open prosjekt.db for å åpne en tom db-fil, men som har ønsket skjema for databasen.
3. Bruk .read sql_insert_data.sql for å sette inn all dataen.

Databasen er da klar til bruk med alle dataene i vedleggene. En ren sql-spørring er for brukstilfelle 5. For å få ønsket
output som beskrevet:

SELECT flyselskap.navn AS Flyselskap, flytypeNavn AS Flytype, Count(flytypeNavn) AS 'Antall fly' FROM Fly
INNER JOIN flyselskap ON fly.flyselskapsKode = flyselskap.flyselskapsKode
GROUP BY flytypeNavn;


