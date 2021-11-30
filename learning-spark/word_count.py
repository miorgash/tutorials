import os
from pyspark import SparkConf, SparkContext
os.chdir('/tmp/work/learning-spark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

rdd = sc.textFile('README.md')

# Transform
words = rdd.flatMap(lambda line: line.split(' '))
result = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

# Action
result.saveAsParquetFile('hoge.parquet')