import os
from pyspark import SparkConf, SparkContext
os.chdir('/tmp/work/learning-spark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()
squared
