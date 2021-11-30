import os
from pyspark import SparkConf, SparkContext
os.chdir('/tmp/work/learning-spark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

lines = sc.textFile('README.md')

# tranform
pythonLines = lines.filter(lambda line: 'Python' in line)
print(pythonLines.first()) # str
print(pythonLines.count())

# tranform
sparkLines = lines.filter(lambda line: 'Spark' in line)
print(sparkLines.first()) # str
print(sparkLines.count())

# transform
psLines = pythonLines.union(sparkLines)
print(psLines.first())
print(psLines.count())

# action
print(psLines.take(5))
print(type(psLines.take(5))) # list
for line in psLines.take(5):
    print(line)

# action
print(psLines.collect())
print(type(psLines.collect())) # list
for line in psLines.collect():
    print(line)