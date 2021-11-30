import os
from pyspark import SparkConf, SparkContext
os.chdir('/tmp/work/learning-spark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

nums = sc.parallelize([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
])
nums.reduce(lambda x, y: x + y)