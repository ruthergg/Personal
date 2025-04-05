-- Daily Refresh
-- Extraction Time stamp
ALTER Table ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
ADD Extraction_TimeStamp TIMESTAMP, 
ADD f_loaded BOOLEAN

update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET f_loaded = TRUE;
update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET Extraction_TimeStamp = now() - INTERVAL 10 DAY;

-- Adding New Sales Transactions
INSERT INTO `salestransaction` (`tid`, `customerid`, `storeid`, `tdate`) VALUES ('ABCD', '0-1-222', 'S1', '2025-03-25');
INSERT INTO `soldvia` (`productid`, `tid`, `noofitems`) VALUES ('1X2', 'ABCD', '1');
INSERT INTO `soldvia` (`productid`, `tid`, `noofitems`) VALUES ('1X1', 'ABCD', '1');
INSERT INTO `rentaltransaction` (`tid`, `customerid`, `storeid`, `tdate`) VALUES ('DCBA', '1-2-333', 'S10', '2025-03-25');
INSERT INTO `rentvia` (`productid`, `tid`, `rentaltype`, `duration`) VALUES ('1X1', 'DCBA', 'D', '10');
INSERT INTO `rentvia` (`productid`, `tid`, `rentaltype`, `duration`) VALUES ('5X5', 'DCBA', 'W', '4');

--Loop Code
Create Table intermediate_facttable as 
select sv.noofitems as UnitsSold, sv.noofitems * p.productprice as RevenueGenerated, sv.tid as TransactionID, "Sales" as RevenueType,
 p.productid as ProductID, st.storeid as StoreID, st.customerid as CustomerID, st.tdate as FullDate
from ruthergg_ZAGIMORE.soldvia sv, ruthergg_ZAGIMORE.product p, ruthergg_ZAGIMORE.salestransaction st
where p.productid = sv.productid and st.tid = sv.tid and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

ALTER table intermediate_facttable Modify RevenueType VARCHAR(20);

insert into intermediate_facttable(UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpricedaily, sv.tid , "Rental,Daily" ,p.productid , st.storeid , st.customerid , st.tdate 
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "D" and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

insert into intermediate_facttable (UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpriceweekly, sv.tid, "Rental,Weekly",p.productid, st.storeid, st.customerid, st.tdate
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "W" and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

insert into Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey, Extraction_TimeStamp, f_loaded)
select i.UnitsSold, i.RevenueGenerated, i.RevenueType, i.TransactionID, cud.CustomerKey, sd.StoreKey, pd.ProductKey, cad.CalendarKey, NOW(), FALSE
From intermediate_facttable i, CustomerDimension cud, StoreDimension sd, ProductDimension pd, CalendarDimension cad
where i.CustomerID = cud.CustomerID and i.storeid = sd.storeid and i.productid = pd.productid and LEFT(pd.ProductType, 1) = LEFT(i.RevenueType,1) and i.FullDate = cad.CalendarDate;

Drop Table intermediate_facttable;

insert into ruthergg_ZAGIMORE_DW.Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey)
select UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey
from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
where f_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET f_loaded = TRUE
where f_loaded = FALSE;

--creating procedure for daily fact refresh
create procedure DailyRegularFactRefresh()
Begin

Create Table intermediate_facttable as 
select sv.noofitems as UnitsSold, sv.noofitems * p.productprice as RevenueGenerated, sv.tid as TransactionID, "Sales" as RevenueType,
 p.productid as ProductID, st.storeid as StoreID, st.customerid as CustomerID, st.tdate as FullDate
from ruthergg_ZAGIMORE.soldvia sv, ruthergg_ZAGIMORE.product p, ruthergg_ZAGIMORE.salestransaction st
where p.productid = sv.productid and st.tid = sv.tid and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

ALTER table intermediate_facttable Modify RevenueType VARCHAR(20);

insert into intermediate_facttable(UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpricedaily, sv.tid , "Rental,Daily" ,p.productid , st.storeid , st.customerid , st.tdate 
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "D" and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

insert into intermediate_facttable (UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpriceweekly, sv.tid, "Rental,Weekly",p.productid, st.storeid, st.customerid, st.tdate
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "W" and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

insert into Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey, Extraction_TimeStamp, f_loaded)
select i.UnitsSold, i.RevenueGenerated, i.RevenueType, i.TransactionID, cud.CustomerKey, sd.StoreKey, pd.ProductKey, cad.CalendarKey, NOW(), FALSE
From intermediate_facttable i, CustomerDimension cud, StoreDimension sd, ProductDimension pd, CalendarDimension cad
where i.CustomerID = cud.CustomerID and i.storeid = sd.storeid and i.productid = pd.productid and LEFT(pd.ProductType, 1) = LEFT(i.RevenueType,1) and i.FullDate = cad.CalendarDate;

Drop Table intermediate_facttable;

insert into ruthergg_ZAGIMORE_DW.Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey)
select UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey
from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
where f_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET f_loaded = TRUE
where f_loaded = FALSE;

END
----------------------------------------------------------------------------------------------------------
--Dimensions
--Daily refresh of product Dimension
ALTER Table ruthergg_ZAGIMORE_DS.ProductDimension
ADD Extraction_TimeStamp TIMESTAMP, 
ADD pd_loaded BOOLEAN

update ruthergg_ZAGIMORE_DS.ProductDimension
SET pd_loaded = TRUE;
update ruthergg_ZAGIMORE_DS.ProductDimension
SET Extraction_TimeStamp = now() - INTERVAL 20 DAY;

-- Adding New Products
INSERT INTO `product` (`productid`, `productname`, `productprice`, `vendorid`, `categoryid`) VALUES ('gyg', 'Rope For Jumping', '1.05', 'OA', 'CP');
INSERT INTO `rentalProducts` (`productid`, `productname`, `vendorid`, `categoryid`, `productpricedaily`, `productpriceweekly`) VALUES ('uyu', 'Rope For Jumping', 'OA', 'CP', '100.01', '700.07');

--Loop Code
--Product
insert into ruthergg_ZAGIMORE_DS.ProductDimension(ProductID, ProductName, ProductPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType, Extraction_TimeStamp, pd_loaded)
select p.productid, p.productname, p.productprice, v.vendorid, v.vendorname, c.categoryid, c.categoryname, "Sales", Now(),FALSE
From ruthergg_ZAGIMORE.product p, ruthergg_ZAGIMORE.category c, ruthergg_ZAGIMORE.vendor v
where p.vendorid = v.vendorid and p.categoryid = c.categoryid and p.productid not in (select ProductID from ruthergg_ZAGIMORE_DS.ProductDimension where ProductType = "Sales")
--Rental Product
insert into  ruthergg_ZAGIMORE_DS.ProductDimension(ProductID, ProductName, ProductDailyRentalPrice, ProductWeeklyRentalPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType, Extraction_TimeStamp, pd_loaded)
select p.productid, p.productname, p.productpricedaily, p.productpriceweekly, v.vendorid, v.vendorname, c.categoryid, c.categoryname, "Rental", Now(),FALSE
From ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.category c, ruthergg_ZAGIMORE.vendor v
where p.vendorid = v.vendorid and p.categoryid = c.categoryid and p.productid not in (select ProductID from ruthergg_ZAGIMORE_DS.ProductDimension where ProductType = "Rental")
--DW Load
insert into ruthergg_ZAGIMORE_DW.ProductDimension(ProductKey, ProductID, ProductName, ProductDailyRentalPrice, 
ProductWeeklyRentalPrice, ProductPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType)
select ProductKey, ProductID, ProductName, ProductDailyRentalPrice, ProductWeeklyRentalPrice, ProductPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType
from ruthergg_ZAGIMORE_DS.ProductDimension where pd_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.ProductDimension
SET pd_loaded = TRUE
where pd_loaded = FALSE;

--Product Refresh
create procedure DailyProductRefresh()
Begin

insert into ruthergg_ZAGIMORE_DS.ProductDimension(ProductID, ProductName, ProductPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType, Extraction_TimeStamp, pd_loaded)
select p.productid, p.productname, p.productprice, v.vendorid, v.vendorname, c.categoryid, c.categoryname, "Sales", Now(),FALSE
From ruthergg_ZAGIMORE.product p, ruthergg_ZAGIMORE.category c, ruthergg_ZAGIMORE.vendor v
where p.vendorid = v.vendorid and p.categoryid = c.categoryid and p.productid not in (select ProductID from ruthergg_ZAGIMORE_DS.ProductDimension where ProductType = "Sales");

insert into  ruthergg_ZAGIMORE_DS.ProductDimension(ProductID, ProductName, ProductDailyRentalPrice, ProductWeeklyRentalPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType, Extraction_TimeStamp, pd_loaded)
select p.productid, p.productname, p.productpricedaily, p.productpriceweekly, v.vendorid, v.vendorname, c.categoryid, c.categoryname, "Rental", Now(),FALSE
From ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.category c, ruthergg_ZAGIMORE.vendor v
where p.vendorid = v.vendorid and p.categoryid = c.categoryid and p.productid not in (select ProductID from ruthergg_ZAGIMORE_DS.ProductDimension where ProductType = "Rental");

insert into ruthergg_ZAGIMORE_DW.ProductDimension(ProductKey, ProductID, ProductName, ProductDailyRentalPrice, 
ProductWeeklyRentalPrice, ProductPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType)
select ProductKey, ProductID, ProductName, ProductDailyRentalPrice, ProductWeeklyRentalPrice, ProductPrice, Vendorid, Vendorname, CategoryID, CategoryName, ProductType
from ruthergg_ZAGIMORE_DS.ProductDimension where pd_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.ProductDimension
SET pd_loaded = TRUE
where pd_loaded = FALSE;

END
--------------------------------------------------------------------------
--Daily refresh of Store Dimension
ALTER Table ruthergg_ZAGIMORE_DS.StoreDimension
ADD Extraction_TimeStamp TIMESTAMP, 
ADD sd_loaded BOOLEAN;

update ruthergg_ZAGIMORE_DS.StoreDimension
SET sd_loaded = TRUE;
update ruthergg_ZAGIMORE_DS.StoreDimension
SET Extraction_TimeStamp = now() - INTERVAL 20 DAY;

-- Adding New store
INSERT INTO `store` (`storeid`, `storezip`, `regionid`) VALUES ('S19', '13456', 'C');
--loop
insert into StoreDimension(StoreID, StoreZip, RegionID, RegionName, Extraction_TimeStamp, sd_loaded)
select s.storeid, s.storezip, r.regionid, r.regionname,Now(),FALSE
from ruthergg_ZAGIMORE.store s, ruthergg_ZAGIMORE.region r
where s.regionid = r.regionid and p.productid not in (select StoreID from ruthergg_ZAGIMORE_DS.StoreDimension);
--Dw load
insert into ruthergg_ZAGIMORE_DW.StoreDimension(StoreKey,StoreID, StoreZip, RegionID, RegionName)
select StoreKey,StoreID, StoreZip, RegionID, RegionName
from ruthergg_ZAGIMORE_DS.StoreDimension where sd_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.StoreDimension
SET sd_loaded = TRUE
where sd_loaded = FALSE;

--Refresh
create procedure DailyStoreRefresh()
Begin

insert into StoreDimension(StoreID, StoreZip, RegionID, RegionName, Extraction_TimeStamp, sd_loaded)
select s.storeid, s.storezip, r.regionid, r.regionname,Now(),FALSE
from ruthergg_ZAGIMORE.store s, ruthergg_ZAGIMORE.region r
where s.regionid = r.regionid and s.storeid not in (select StoreID from ruthergg_ZAGIMORE_DS.StoreDimension);

insert into ruthergg_ZAGIMORE_DW.StoreDimension(StoreKey,StoreID, StoreZip, RegionID, RegionName)
select StoreKey,StoreID, StoreZip, RegionID, RegionName
from ruthergg_ZAGIMORE_DS.StoreDimension where sd_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.StoreDimension
SET sd_loaded = TRUE
where sd_loaded = FALSE;

END
-------------------------------------------------------------------------------------------------------
--Customer Dimension
ALTER Table ruthergg_ZAGIMORE_DS.CustomerDimension
ADD Extraction_TimeStamp TIMESTAMP, 
ADD cd_loaded BOOLEAN;

update ruthergg_ZAGIMORE_DS.CustomerDimension
SET cd_loaded = TRUE;
update ruthergg_ZAGIMORE_DS.CustomerDimension
SET Extraction_TimeStamp = now() - INTERVAL 20 DAY;

--adding new customers
INSERT INTO `customer` (`customerid`, `customername`, `customerzip`) VALUES ('0-4-199', 'TY Chuck', '13456');
--loop
insert into CustomerDimension(CustomerId, CustomerName, CustomerZip, Extraction_TimeStamp, cd_loaded)
select c.customerid, c.customername, c.customerzip,Now(),FALSE
from ruthergg_ZAGIMORE.customer c
where c.customerid not in (select CustomerID from ruthergg_ZAGIMORE_DS.CustomerDimension);
--dw load
insert into ruthergg_ZAGIMORE_DW.CustomerDimension(CustomerKey, CustomerId, CustomerName, CustomerZip)
select c.CustomerKey, c.CustomerId, c.CustomerName, c.CustomerZip
from ruthergg_ZAGIMORE_DS.CustomerDimension c

update ruthergg_ZAGIMORE_DS.CustomerDimension
SET cd_loaded = TRUE
where cd_loaded = FALSE;

--refresh
create procedure DailyCustomerRefresh()
Begin

insert into CustomerDimension(CustomerId, CustomerName, CustomerZip, Extraction_TimeStamp, cd_loaded)
select c.customerid, c.customername, c.customerzip,Now(),FALSE
from ruthergg_ZAGIMORE.customer c
where c.customerid not in (select CustomerID from ruthergg_ZAGIMORE_DS.CustomerDimension);

insert into ruthergg_ZAGIMORE_DW.CustomerDimension(CustomerKey, CustomerId, CustomerName, CustomerZip)
select c.CustomerKey, c.CustomerId, c.CustomerName, c.CustomerZip
from ruthergg_ZAGIMORE_DS.CustomerDimension c where c.cd_loaded = FALSE

update ruthergg_ZAGIMORE_DS.CustomerDimension
SET cd_loaded = TRUE
where cd_loaded = FALSE;

END

-- Late Fact Arrivel Refresh
-- Extraction Time stamp
ALTER Table ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
ADD Extraction_TimeStamp TIMESTAMP, 
ADD f_loaded BOOLEAN

update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET f_loaded = TRUE;
update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET Extraction_TimeStamp = now() - INTERVAL 10 DAY;

-- Adding New Sales Transactions
INSERT INTO `salestransaction` (`tid`, `customerid`, `storeid`, `tdate`) VALUES ('PPPP', '0-1-222', 'S1', '2025-03-25');
INSERT INTO `soldvia` (`productid`, `tid`, `noofitems`) VALUES ('1X2', 'PPPP', '1');
INSERT INTO `soldvia` (`productid`, `tid`, `noofitems`) VALUES ('1X1', 'PPPP', '1');
INSERT INTO `rentaltransaction` (`tid`, `customerid`, `storeid`, `tdate`) VALUES ('OOOO', '1-2-333', 'S10', '2025-03-25');
INSERT INTO `rentvia` (`productid`, `tid`, `rentaltype`, `duration`) VALUES ('1X1', 'OOOO', 'D', '10');
INSERT INTO `rentvia` (`productid`, `tid`, `rentaltype`, `duration`) VALUES ('5X5', 'OOOO', 'W', '4');

--Loop Code
Create Table intermediate_facttable as 
select sv.noofitems as UnitsSold, sv.noofitems * p.productprice as RevenueGenerated, sv.tid as TransactionID, "Sales" as RevenueType,
 p.productid as ProductID, st.storeid as StoreID, st.customerid as CustomerID, st.tdate as FullDate
from ruthergg_ZAGIMORE.soldvia sv, ruthergg_ZAGIMORE.product p, ruthergg_ZAGIMORE.salestransaction st
where p.productid = sv.productid and st.tid = sv.tid and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

ALTER table intermediate_facttable Modify RevenueType VARCHAR(20);

insert into intermediate_facttable(UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpricedaily, sv.tid , "Rental,Daily" ,p.productid , st.storeid , st.customerid , st.tdate 
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "D" and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

insert into intermediate_facttable (UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpriceweekly, sv.tid, "Rental,Weekly",p.productid, st.storeid, st.customerid, st.tdate
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "W" and st.tdate > (select  MAX(date(Extraction_TimeStamp)) from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension);

insert into Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey, Extraction_TimeStamp, f_loaded)
select i.UnitsSold, i.RevenueGenerated, i.RevenueType, i.TransactionID, cud.CustomerKey, sd.StoreKey, pd.ProductKey, cad.CalendarKey, NOW(), FALSE
From intermediate_facttable i, CustomerDimension cud, StoreDimension sd, ProductDimension pd, CalendarDimension cad
where i.CustomerID = cud.CustomerID and i.storeid = sd.storeid and i.productid = pd.productid and LEFT(pd.ProductType, 1) = LEFT(i.RevenueType,1) and i.FullDate = cad.CalendarDate;

Drop Table intermediate_facttable;

insert into ruthergg_ZAGIMORE_DW.Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey)
select UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey
from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
where f_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET f_loaded = TRUE
where f_loaded = FALSE;

--creating procedure for daily fact refresh
create procedure LateArrivingFactRefresh()
Begin

Create Table intermediate_facttable as 
select sv.noofitems as UnitsSold, sv.noofitems * p.productprice as RevenueGenerated, sv.tid as TransactionID, "Sales" as RevenueType,
 p.productid as ProductID, st.storeid as StoreID, st.customerid as CustomerID, st.tdate as FullDate
from ruthergg_ZAGIMORE.soldvia sv, ruthergg_ZAGIMORE.product p, ruthergg_ZAGIMORE.salestransaction st
where p.productid = sv.productid and st.tid = sv.tid and st.tid not in (select TransactionID from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension where RevenueType = "Sales");

ALTER table intermediate_facttable Modify RevenueType VARCHAR(20);

insert into intermediate_facttable(UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpricedaily, sv.tid , "Rental,Daily" ,p.productid , st.storeid , st.customerid , st.tdate 
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "D" and st.tid not in (select TransactionID from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension where RevenueType like "R%");

insert into intermediate_facttable (UnitsSold,RevenueGenerated,TransactionID,RevenueType,ProductID,StoreID,CustomerID,FullDate)
select 0 , sv.duration * p.productpriceweekly, sv.tid, "Rental,Weekly",p.productid, st.storeid, st.customerid, st.tdate
from ruthergg_ZAGIMORE.rentvia sv, ruthergg_ZAGIMORE.rentalProducts p, ruthergg_ZAGIMORE.rentaltransaction st
where p.productid = sv.productid and st.tid = sv.tid and sv.rentaltype = "W" and st.tid not in (select TransactionID from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension where RevenueType like "R%");

insert into Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey, Extraction_TimeStamp, f_loaded)
select i.UnitsSold, i.RevenueGenerated, i.RevenueType, i.TransactionID, cud.CustomerKey, sd.StoreKey, pd.ProductKey, cad.CalendarKey, NOW(), FALSE
From intermediate_facttable i, CustomerDimension cud, StoreDimension sd, ProductDimension pd, CalendarDimension cad
where i.CustomerID = cud.CustomerID and i.storeid = sd.storeid and i.productid = pd.productid and LEFT(pd.ProductType, 1) = LEFT(i.RevenueType,1) and i.FullDate = cad.CalendarDate;

Drop Table intermediate_facttable;

insert into ruthergg_ZAGIMORE_DW.Revenue_and_Units_Dimension(UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey)
select UnitsSold, RevenueGenerated, RevenueType, TransactionID, CustomerKey, StoreKey, ProductKey, CalendarKey
from ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
where f_loaded = FALSE;

update ruthergg_ZAGIMORE_DS.Revenue_and_Units_Dimension
SET f_loaded = TRUE
where f_loaded = FALSE;

END