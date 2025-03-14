BEGIN TRANSACTION;
INSERT INTO flyplass VALUES('BOO','Bodo Lufthavn');
INSERT INTO flyplass VALUES('BGO','Bergen Lufthavn, Flesland');
INSERT INTO flyplass VALUES('OSL','Oslo Lufthavn, Gardermoen');
INSERT INTO flyplass VALUES('SVG','Stavanger Lufthavn, Sola');
INSERT INTO flyplass VALUES('TRD','Trondheim Lufthavn, Værnes');

INSERT INTO Flyselskap VALUES('DY','Norwegian');
INSERT INTO Flyselskap VALUES('SK','SAS');
INSERT INTO Flyselskap VALUES('WF','Wideroe');

INSERT INTO Flytype VALUES('Boeing 737 800',1997,2020);
INSERT INTO Flytype VALUES('Airbus a320neo',2016,NULL);
INSERT INTO Flytype VALUES('Dash-8 100',1984,2005);

INSERT INTO flyprodusent VALUES('The Boeing Company','Amerikansk',1916);
INSERT INTO flyprodusent VALUES('Airbus Group','Fransk, Tysk, Spansk, Britisk',1970);
INSERT INTO flyprodusent VALUES('De Havilland','Kanadisk',1920);

INSERT INTO Fly VALUES('LN-ENU',42069,NULL,2015,'Boeing 737 800','DY','The Boeing Company');
INSERT INTO Fly VALUES('LN-ENR',42093,'Jan Baalsrud',2018,'Boeing 737 800','DY','The Boeing Company');
INSERT INTO Fly VALUES('LN-NIQ',39403,'Max Manus',2011,'Boeing 737 800','DY','The Boeing Company');
INSERT INTO Fly VALUES('LN-ENS',42281,NULL,2017,'Boeing 737 800','DY','The Boeing Company');
INSERT INTO Fly VALUES('SE-RUB',9518,'Birger Viking',2020,'Airbus a320neo','SK','Airbus Group');
INSERT INTO Fly VALUES('SE-DIR',11421,'Nora Viking',2023,'Airbus a320neo','SK','Airbus Group');
INSERT INTO Fly VALUES('SE-RUP',12066,'Ragnhild Viking',2024,'Airbus a320neo','SK','Airbus Group');
INSERT INTO Fly VALUES('SE-RZE',12166,'Ebbe Viking',2024,'Airbus a320neo','SK','Airbus Group');
INSERT INTO Fly VALUES('LN-WIH',383,'Oslo',1994,'Dash-8 100','WF','De Havilland');
INSERT INTO Fly VALUES('LN-WIA',359,'Nordland',1993,'Dash-8 100','WF','De Havilland');
INSERT INTO Fly VALUES('LN-WIL',298,'Narvik',1995,'Dash-8 100','WF','De Havilland');

INSERT INTO konfigurasjon VALUES(6,31,'ABCDEF','13','Boeing 737 800');
INSERT INTO konfigurasjon VALUES(6,30,'ABCDEF','11-12','Airbus a320neo');
INSERT INTO konfigurasjon VALUES(4,10,'ABCD','5','Dash-8 100');

INSERT INTO Flyruter VALUES('WF1311',12345,'16:20:00','15:15:00',NULL,NULL,'WF','Dash-8 100');
INSERT INTO Flyruter VALUES('WF1302',12345,'08:40:00','07:35:00',NULL,NULL,'WF','Dash-8 100');
INSERT INTO Flyruter VALUES('DY753',1234567,'11:15:00','10:20:00',NULL,NULL,'DY','Boeing 737 800');
INSERT INTO Flyruter VALUES('SK332',1234567,'09:05:00','08:00:00',NULL,NULL,'DY','Airbus a320neo');
INSERT INTO Flyruter VALUES('SK888',12345,'12:10:00','10:00:00',NULL,NULL,'DY','Airbus a320neo');

INSERT INTO Delreise VALUES('SK888',1,'11:10:00','10:00:00','BGO','TRD');
INSERT INTO Delreise VALUES('SK888',2,'12:10:00','11:40:00','SVG','BGO');
INSERT INTO Delreise VALUES('SK888',3,'12:10:00','11:40:00','TRD','BGO');
INSERT INTO Delreise VALUES('WF1311',1,'16:20:00','15:15:00', 'BOO', 'TRD');
INSERT INTO Delreise VALUES('WF1302',1,'08:40:00','07:35:00', 'TRD', 'BOO');
INSERT INTO Delreise VALUES('DY753',1,'11:15:00','10:20:00', 'OSL', 'TRD');
INSERT INTO Delreise VALUES('SK332',1,'09:05:00','08:00:00', 'TRD', 'OSL');

INSERT INTO Kunde VALUES(1,'Per Person',98888888,'per@admin.no','Norsk');
INSERT INTO Kunde VALUES(2,'Inger Person',98888887,'inger@admin.no','Norsk');

INSERT INTO Flyvning VALUES(1,'WF1302','Planned','LN-WIA','2025-04-01');
INSERT INTO Flyvning VALUES(1,'DY753','Planned','LN-ENR','2025-04-01');
INSERT INTO Flyvning VALUES(1,'SK888','Planned','SE-DIR','2025-04-01');

INSERT INTO Flybillettpris VALUES ('premium','WF1302', 1, 2018, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','WF1302', 1, 899, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','WF1302', 1, 599, NULL);
INSERT INTO Flybillettpris VALUES ('premium','WF1311', 1, 2018, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','WF1311', 1, 899, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','WF1311', 1, 599, NULL);
INSERT INTO Flybillettpris VALUES ('premium','DY753', 1, 1500, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','DY753', 1, 1000, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','DY753', 1, 500, NULL);
INSERT INTO Flybillettpris VALUES ('premium','SK332', 1, 1500, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','SK332', 1, 1000, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','SK332', 1, 500, NULL);
INSERT INTO Flybillettpris VALUES ('premium','SK888', 1, 2000, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','SK888', 1, 1500, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','SK888', 1, 800, NULL);
INSERT INTO Flybillettpris VALUES ('premium','SK888', 2, 1000, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','SK888', 2, 700, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','SK888', 2, 350, NULL);
INSERT INTO Flybillettpris VALUES ('premium','SK888', 3, 2200, NULL);
INSERT INTO Flybillettpris VALUES ('okonomi','SK888', 3, 1700, NULL);
INSERT INTO Flybillettpris VALUES ('budsjett','SK888', 3, 1000, NULL);

INSERT INTO Sete VALUES(1,'WF1302','A',8,1);
INSERT INTO Sete VALUES(1,'WF1302','B',8,1);
INSERT INTO Sete VALUES(1,'WF1302','C',8,1);
INSERT INTO Sete VALUES(1,'WF1302','A',9,1);
INSERT INTO Sete VALUES(1,'WF1302','B',9,1);
INSERT INTO Sete VALUES(1,'WF1302','D',9,1);
INSERT INTO Sete VALUES(1,'WF1302','A',10,1);
INSERT INTO Sete VALUES(1,'WF1302','C',10,1);
INSERT INTO Sete VALUES(1,'WF1302','B',2,1);
INSERT INTO Sete VALUES(1,'WF1302','A',3,1);

INSERT INTO Flybillett VALUES(1,1,1,'WF1302',1,'premium');
INSERT INTO Flybillett VALUES(2,1,1,'WF1302',1,'premium');
INSERT INTO Flybillett VALUES(3,1,1,'WF1302',1,'premium');
INSERT INTO Flybillett VALUES(4,1,1,'WF1302',1,'premium');
INSERT INTO Flybillett VALUES(5,1,1,'WF1302',1,'premium');
INSERT INTO Flybillett VALUES(6,1,1,'WF1302',1,'okonomi');
INSERT INTO Flybillett VALUES(7,1,1,'WF1302',1,'okonomi');
INSERT INTO Flybillett VALUES(8,1,1,'WF1302',1,'okonomi');
INSERT INTO Flybillett VALUES(9,1,1,'WF1302',1,'okonomi');
INSERT INTO Flybillett VALUES(10,1,1,'WF1302',1,'budsjett');
COMMIT;
