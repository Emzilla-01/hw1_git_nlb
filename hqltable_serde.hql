create database if not exists xmldb;
use xmldb;

create table ebay_tbl (seller_name string,
seller_rating BIGINT, bidder_name string, location string, 
bid_history map <string, string>)

ROW FORMAT SERDE 'com.ibm.sbss.hive.serde2.xml.XmlSerDe'

WITH SERDEPROPERTIES (
"column.xpath.seller_name"="/listing/seller_info/seller_name/text()", 
"column.xpath.seller_rating"="/listing/seller_info/seller_rating/text()", 
"column.xpath.bidder_name"="/listing/auction_info/high_bidder/bidder_name/text()",
"column.xpath.location"="/listing/auction_info/location/text()",
"column.xpath.bid_history"="/listing/bid_history/*",
"column.xpath.item_info"="/listing/item_info/*"
)

STORED AS 

INPUTFORMAT 'com.ibm.sbss.hive.serde2.xml.XmlInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'

TBLPROPERTIES(
"xmlinput.start"= "<listing>",
"xmlinput.end" = "</listing>"
);

LOAD DATA LOCAL INPATH '/home/hadoop/ebay.xml'
OVERWITE INTO TABLE ebay_tbl;
