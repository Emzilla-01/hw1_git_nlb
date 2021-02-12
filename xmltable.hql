create database if not exists xmldatabase;

use xmldatabase;

drop table if exists xml_table;
create external table if not exists xml_table (xml_str string);

load data local inpath '/home/hadoop/dataset.xml' into table xml_table;

--select xpath(xml_str, 'dataset/record/first_name/text()') as fname, xpath(xml_str, 'dataset/record/gender/text()') as g from xml_table limit 20;

drop view if exists myview;
create view myview (id, name, gender, country)
as select
xpath(xml_str, 'record/id/text()'),
xpath(xml_str, 'record/first_name/text()'),
xpath(xml_str, 'record/gender/text()'),
xpath(xml_str, 'record/country/text()')
from xml_table;

select * from myview limit 20;


