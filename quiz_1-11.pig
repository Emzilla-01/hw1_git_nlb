data_ = LOAD 'hdfs://localhost:9000/pig/movies_data.csv' using PigStorage(',') AS (ix:int, title:chararray, year:int, rating:float, votes:int);

g0 = group data_ all;
c0 = foreach g0 generate COUNT(data_);

f0 = filter data_ by not ($0 < 0 and $1 == '' and $2 < 0 and $3 < 0 and $4 < 0);

g1 = group f0 all;
c1 = foreach g1 generate COUNT(f0);

g2 = group f0 by year;

each_year_ratings = foreach g2 generate(MAX(f0.year), MAX(f0.rating));

answer_c = join f0 by (year, rating), each_year_ratings by ($0.$0, $0.$1);/*best movies for each year!*/

--store answer_c into '/pig/output';

d_filt = filter f0 by (year >= 2005);
d_ord = ORDER d_filt by rating DESC;
d_lim = LIMIT d_ord 10;
dump d_lim;


e_grp = group f0 by (rating);

answer_e = FOREACH e_grp GENERATE (group, SIZE(f0.title));
dump answer_e;
