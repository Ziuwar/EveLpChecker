
drop database evedata;

create database evedata;

-----------------------------------

CREATE TABLE EveMineralPrice (

	Mineral varchar(50) NOT NULL PRIMARY KEY,
	ItemUid int,
	ItemPrice float
	
);

-----------------------------------

CREATE TABLE EvePriceHistory (

	Ident int AUTO_INCREMENT NOT NULL PRIMARY KEY,
	EveItemId int,
	PriceTimestamp date
);

------------------------------------

CREATE TABLE EveItemData (

	ItemUid int NOT NULL PRIMARY KEY,
	ItemName varchar (100),
	IskPrice float,
	LpPoints int,
	MaterialPrice float,
	ItemTotalPrice float,
	SellPriceJita float,
	SellTaxes float,
	Profit float,
	ProfitPercent float,
	Efficiency float,
	Tritanium int,
	Pyerite int,
	Mexallon int,
	Isogen int,
	Nocxium int,
	Zydrine int,
	Megacyte int
);

------------------------------------

INSERT INTO EveMineralPrice
	VALUES
	('Tritanium','34', '4.79'),
	('Pyerite','35', '5.20'),
	('Mexallon','36', '63.80'),
	('Isogen', '37', '70.00'),
	('Nocxium', '38', '416.99'),
	('Zydrine', '39', '1309.89'),
	('Megacyte', '40', '1090.00');


------------------------------------





