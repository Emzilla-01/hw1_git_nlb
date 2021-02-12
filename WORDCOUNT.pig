input_ = LOAD 'hdfs://localhost:9000/pig/TaintedLove.txt' AS (line:Chararray);
Words = FOREACH input_ GENERATE FLATTEN(TOKENIZE(line, ' ')) AS word;
grouped = GROUP Words by word;
wordcount = FOREACH grouped GENERATE group, COUNT(Words);
dump wordcount;
