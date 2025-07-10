CREATE TABLE ProductDimension
(
  ProductKey INT NOT NULL,
  ProductID CHAR(3) NOT NULL,
  ProductName VARCHAR(25) NOT NULL,
  Vendorid CHAR(2) NOT NULL,
  Vendorname VARCHAR(25) NOT NULL,
  CategoryID CHAR(2) NOT NULL,
  CategoryName VARCHAR(25) NOT NULL,
  ProductType VarCHAR(8) NOT NULL,
  ProductPrice NUMERIC(7,2),
  ProductWeeklyRentalPrice NUMERIC(7,2),
  ProductDailyRentalPrice NUMERIC(7,2),
  PRIMARY KEY (ProductKey)
);

CREATE TABLE CustomerDimension
(
  CustomerKey INT NOT NULL,
  CustomerID CHAR(7) NOT NULL,
  CustomerName VARCHAR(15) NOT NULL,
  CustomerZip CHAR(5) NOT NULL,
  PRIMARY KEY (CustomerKey)
);

CREATE TABLE CalendarDimension
(
  CalendarKey INT NOT NULL,
  CalendarDate DATE NOT NULL,
  CalendarMonth INT NOT NULL,
  CalendarYear INT NOT NULL,
  PRIMARY KEY (CalendarKey)
);

CREATE TABLE StoreDimension
(
  StoreKey INT NOT NULL,
  StoreID VARCHAR(3) NOT NULL,
  StoreZip CHAR(5) NOT NULL,
  RegionID CHAR(1) NOT NULL,
  RegionName VARCHAR(25) NOT NULL,
  PRIMARY KEY (StoreKey)
);

CREATE TABLE Revenue_and_Units_Dimension
(
  RevenueGenerated INT NOT NULL,
  UnitsSold INT NOT NULL,
  TransactionID VARCHAR(8) NOT NULL,
  RevenueType VARCHAR(8) NOT NULL,
  ProductKey INT NOT NULL,
  CustomerKey INT NOT NULL,
  CalendarKey INT NOT NULL,
  StoreKey INT NOT NULL,
  PRIMARY KEY (TransactionID, RevenueType, ProductKey, CustomerKey, CalendarKey, StoreKey),
  FOREIGN KEY (ProductKey) REFERENCES ProductDimension(ProductKey),
  FOREIGN KEY (CustomerKey) REFERENCES CustomerDimension(CustomerKey),
  FOREIGN KEY (CalendarKey) REFERENCES CalendarDimension(CalendarKey),
  FOREIGN KEY (StoreKey) REFERENCES StoreDimension(StoreKey)
);