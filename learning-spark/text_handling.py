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

splittedLines = pythonLines.map(lambda line: line.split())
for line in splittedLines.take(2):
    print(line)