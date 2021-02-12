
create database if not exists XMLDb;

use XMLDb;

create table if not exists ebay_table (seller_name STRING,
seller_rating BIGINT, bidder_name STRING, location STRING, bid_history map <string, string>,
item_info map <string, string>)

ROW FORMAT SERDE 'com.ibm.spss.hive.serde2.xml.XmlSerDe'
WITH SERDEPROPERTIES (
"column.xpath.seller_name"="/listing/seller_info/seller_name/text()",
"column.xpath.seller_rating"="/listing/seller_info/seller_rating/text()",
"column.xpath.bidder_name"="/listing/auction_info/high_bidder/bidder_name/text()",
"column.xpath.location"="/listing/auction_info/location/text()",
"column.xpath.bid_history"="/listing/bid_history/*",
"column.xpath.item_info"="/listing/item_info/*"
)

STORED AS
INPUTFORMAT 'com.ibm.spss.hive.serde2.xml.XmlInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'

TBLPROPERTIES (
"xmlinput.start"="<listing>",
"xmlinput.end"="</listing>");


LOAD DATA LOCAL INPATH '/home/hadoop/ebay.xml'
OVERWRITE INTO TABLE ebay_table;

SELECT seller_name, bidder_name, location, bid_history["highest_bid_amount"], item_info["cpu"], item_info["memory"] from ebay_table limit 5;

SELECT distinct(location) from ebay_table;
