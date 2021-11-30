import os
from pyspark import SparkConf, SparkContext
os.chdir('/tmp/work/learning-spark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

lines = sc.textFile('README.md')
print(type(lines)) # RDD
print(lines.count())

pythonLines = lines.filter(lambda line: 'Python' in line)
print(type(pythonLines)) # PipelinedRDD
print(type(pythonLines.first())) # str
print(pythonLines.first())
print(pythonLines.count())