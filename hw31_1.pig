rmf /output/hw31

product_data = LOAD 'hdfs://localhost:9000/data/Product.csv' using PigStorage('\t') AS
(ProductID:int,
Name:chararray,
ProductNumber:chararray,
MakeFlag:int,
FinishedGoodsFlag:int,
Color:chararray,
SafetyStockLevel:chararray,
ReorderPoint:chararray,
StandardCost:chararray,
ListPrice:chararray,
Size:chararray,
SizeUnitMeasureCode:chararray,
WeightUnitMeasureCode:chararray,
Weight:chararray,
DaysToManufacture:chararray,
ProductLine:chararray,
Class:chararray,
Style:chararray,
ProductSubcategoryID:chararray,
ProductModelID:chararray,
SellStartDate:chararray,
SellEndDate:chararray,
DiscontinuedDate:chararray,
Rowguid:chararray,
ModifiedDate:chararray);


sales_data = LOAD 'hdfs://localhost:9000/data/SalesOrderDetail.csv' using PigStorage('\t') AS
(
SalesOrderID: int,
SalesOrderDetailID: int,
CarrierTrackingNumber: chararray,
OrderQty: int,
ProductID: int,
SpecialOfferID: int, 
UnitPrice: double,
UnitPriceDiscount: float,
LineTotal: double,
rowguid: chararray,
ModifiedDate: chararray
);

a_answer0 = foreach product_data generate Name;
a_answer1i = foreach product_data generate ProductSubcategoryID;
a_answer2i = foreach sales_data generate SalesOrderDetailID;

a_answer1f = DISTINCT a_answer1i;
a_answer2f = DISTINCT a_answer2i;
store a_answer0 into '/output/hw31/a0';
store a_answer1f into '/output/hw31/a1';
store a_answer2f into '/output/hw31/a2';


--foo = foreach a_answer2f generate sales_data::a_answer2f as sd;

b_answer = join sales_data by ProductID, product_data by ProductID;
c = filter b_answer by (OrderQty > 0);
c1 = limit c 10;

d = foreach c generate product_data::ProductID, sales_data::ProductID, product_data::Name, product_data::ProductNumber, sales_data::OrderQty, sales_data::LineTotal;

e = GROUP d by (product_data::ProductID, product_data::ProductNumber, sales_data::OrderQty, sales_data::LineTotal); 

e1 = limit e 10;
dump e1;

-- f foreach e generate
