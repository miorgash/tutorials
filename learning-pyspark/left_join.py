import os
from pyspark import SparkConf, SparkContext
os.chdir('/tmp/work/learning-pyspark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

rdd1 = sc.parallelize([('a', 1), ('b', 4), ('c', 10)])
rdd2 = sc.parallelize([('a', 4), ('a', 1), ('b', 6), ('d', 15)])
rdd3 = rdd1.leftOuterJoin(rdd2)
rdd3.collect()