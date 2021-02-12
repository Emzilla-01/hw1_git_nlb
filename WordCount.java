import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {
   public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
    }
  }

  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    //reads the default configuration of cluster from the configuration xml files
    Configuration conf = new Configuration();
    
    //Initializing the job with the default configuration of the cluster	
    Job job = Job.getInstance(conf, "word count");
    
    //Assigning the driver class name
    job.setJarByClass(WordCount.class);
    
    //setting up Mapper class
    job.setMapperClass(TokenizerMapper.class);
    
    //setting up combiner class  
    job.setCombinerClass(IntSumReducer.class);
    
    // setting up reducer class
    job.setReducerClass(IntSumReducer.class);
    
    //Key type coming out of mapper
    job.setOutputKeyClass(Text.class);
    
    //value type coming out of mapper
    job.setOutputValueClass(IntWritable.class);

    //Defining input Format class which is responsible to parse the dataset into a key value pair
    FileInputFormat.addInputPath(job, new Path(args[0]));
    
    //Defining output Format class which is responsible to parse the dataset into a key value pair
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    
    //exiting the job only if the flag value becomes false
    System.exit(job.waitForCompletion(true) ? 0 : 1);

  }
}
