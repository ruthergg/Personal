--OneWayAggByProductCategory
create table ProductCategoryDimension as
select distinct CategoryID, CategoryName
from Product Dimension

alter table ProductCategoryDimension
add Column CategoryKey Int Auto_Increment Primary Key 

create table OneWayAggByProductCategory as
select SUM(r.UnitsSold) as TotalUnitsSold, SUM(r.RevenueGenerated), r.CustomerKey, r.CalendarKey, r.StoreKey, pcd.CategoryKey
from Revenue_and_Units_Dimension r, ProductCategoryDimension pcd, ProductDimension pd
where pd.ProductKey = r.ProductKey and pd.CategoryID = pcd.CategoryID
group by r.CustomerKey, r.CalendarKey, r.StoreKey, pcd.CategoryKey

ALTER TABLE `OneWayAggByProductCategory` ADD PRIMARY KEY(`CustomerKey`, `CalendarKey`, `StoreKey`, `CategoryKey`);

create table ruthergg_ZAGIMORE_DW.ProductCategoryDimension as
select *
from ruthergg_ZAGIMORE_DS.ProductCategoryDimension

ALTER TABLE `ProductCategoryDimension` ADD PRIMARY KEY(`CategoryKey`);

create table ruthergg_ZAGIMORE_DW.OneWayAggByProductCategory as
select *
from ruthergg_ZAGIMORE_DS.OneWayAggByProductCategory

ALTER TABLE `OneWayAggByProductCategory` ADD PRIMARY KEY(`CustomerKey`, `CalendarKey`, `StoreKey`, `CategoryKey`);

ALTER TABLE ruthergg_ZAGIMORE_DW.OneWayAggByProductCategory ADD Foreign Key(CalendarKey) REFERENCES ruthergg_ZAGIMORE_DW.CalendarDimension(CalendarKey)
ALTER TABLE ruthergg_ZAGIMORE_DW.OneWayAggByProductCategory ADD Foreign Key(CustomerKey) REFERENCES ruthergg_ZAGIMORE_DW.CustomerDimension(CustomerKey)
ALTER TABLE ruthergg_ZAGIMORE_DW.OneWayAggByProductCategory ADD Foreign Key(CategoryKey) REFERENCES ruthergg_ZAGIMORE_DW.ProductCategoryDimension(CategoryKey);
ALTER TABLE ruthergg_ZAGIMORE_DW.OneWayAggByProductCategory ADD Foreign Key(StoreKey) REFERENCES ruthergg_ZAGIMORE_DW.StoreDimension(StoreKey);

-- Daily store Snap Shot
create table DailyStoreSnapShot as
select SUM(r.UnitsSold) as TotalUnitsSold, SUM(r.RevenueGenerated) as TotalRevenueGenerated, r.CalendarKey,COUNT(distinct r.TransactionID) as TotalNumberTransactions, AVG(r.RevenueGenerated) as AverageRevenue,r.StoreKey
from Revenue_and_Units_Dimension r
group by  r.CalendarKey, r.StoreKey

create table ruthergg_ZAGIMORE_DW.DailyStoreSnapShot as
select *
from ruthergg_ZAGIMORE_DS.DailyStoreSnapShot

ALTER TABLE ruthergg_ZAGIMORE_DW.DailyStoreSnapShot ADD PRIMARY KEY(`CalendarKey`, `StoreKey`);

ALTER TABLE ruthergg_ZAGIMORE_DW.DailyStoreSnapShot ADD Foreign Key(CalendarKey) REFERENCES ruthergg_ZAGIMORE_DW.CalendarDimension(CalendarKey);
ALTER TABLE ruthergg_ZAGIMORE_DW.DailyStoreSnapShot ADD Foreign Key(StoreKey) REFERENCES ruthergg_ZAGIMORE_DW.StoreDimension(StoreKey);

--total footware revenue colunm
alter table DailyStoreSnapShot 
add COLUMN TotalFootwearRevenue Decimal(10,0) Default 0;

create table FootwearRevenue as 
select SUM(r.RevenueGenerated) as TotalFootwareRevenue, r.CalendarKey,r.StoreKey
from Revenue_and_Units_Dimension r, ProductDimension pd
where pd.ProductKey = r.ProductKey and pd.CategoryName = "Footwear"
group by  r.CalendarKey, r.StoreKey

update DailyStoreSnapShot ds, FootwearRevenue fw 
set TotalFootwearRevenue = fw.TotalFootwareRevenue
where ds.CalendarKey = fw.CalendarKey and ds.StoreKey = fw.StoreKey

-- Local Customers
alter table DailyStoreSnapShot 
add COLUMN TotalLocalRevenue Decimal(10,0) Default 0;

create table LocalRevenue as 
select SUM(r.RevenueGenerated) as TotalLocalRevenue, r.CalendarKey,r.StoreKey
from Revenue_and_Units_Dimension r, CustomerDimension cd, StoreDimension sd
where sd.StoreKey = r.StoreKey and cd.CustomerKey = r.CustomerKey and left(cd.CustomerZip, 2) = left(sd.StoreZip, 2)
group by  r.CalendarKey, r.StoreKey

update DailyStoreSnapShot ds, LocalRevenue LR 
set ds.TotalLocalRevenue = LR.TotalLocalRevenue
where ds.CalendarKey = LR.CalendarKey and ds.StoreKey = LR.StoreKey

-- number of transaciton over 100 dollars
alter table DailyStoreSnapShot 
add COLUMN HighValueTransactionCount INT Default 0;
 
(select TransactionID
from Revenue_and_Units_Dimension
group by TransactionID
Having SUM(RevenueGenerated) > 100)

create table HighValueTransaction as 
select Count(distinct r.TransactionID) as HighValueTransactionCount, r.CalendarKey,r.StoreKey
from Revenue_and_Units_Dimension r
where r.TransactionID in (select TransactionID from Revenue_and_Units_Dimension group by TransactionID Having SUM(RevenueGenerated) > 100)
group by  r.CalendarKey, r.StoreKey

update DailyStoreSnapShot ds, HighValueTransaction HVT
set ds.HighValueTransactionCount = HVT.HighValueTransactionCount
where ds.CalendarKey = HVT.CalendarKey and ds.StoreKey = HVT.StoreKey

--Load to DW

create table ruthergg_ZAGIMORE_DW.DailyStoreSnapShot as
select *
from ruthergg_ZAGIMORE_DS.DailyStoreSnapShot

ALTER TABLE ruthergg_ZAGIMORE_DW.DailyStoreSnapShot ADD PRIMARY KEY(`CalendarKey`, `StoreKey`);

ALTER TABLE ruthergg_ZAGIMORE_DW.DailyStoreSnapShot ADD Foreign Key(CalendarKey) REFERENCES ruthergg_ZAGIMORE_DW.CalendarDimension(CalendarKey);
ALTER TABLE ruthergg_ZAGIMORE_DW.DailyStoreSnapShot ADD Foreign Key(StoreKey) REFERENCES ruthergg_ZAGIMORE_DW.StoreDimension(StoreKey);