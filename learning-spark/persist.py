import os
from pyspark import SparkConf, SparkContext
from datetime import datetime
os.chdir('/tmp/work/learning-spark')
# create context
conf = SparkConf().setMaster('local').setAppName('MyApp')
sc = SparkContext.getOrCreate(conf = conf)

lines = sc.textFile('README.md')

# transform
pythonLines = lines.filter(lambda line: 'Python' in line)

# w/o persist
start = datetime.now()
_ = pythonLines.count()
first = datetime.now()
_ = pythonLines.count()
second = datetime.now()
print('1 回目:', first - start)
print('2 回目:', second - first)
# 1 回目: 0:00:00.492716
# 2 回目: 0:00:00.329099
# -> 大して速くなってない

# w/persist
pythonLines.persist()
start = datetime.now()
_ = pythonLines.count()
first = datetime.now()
_ = pythonLines.count()
second = datetime.now()
print('1 回目:', first - start)
print('2 回目:', second - first)
# 1 回目: 0:00:00.250059
# 2 回目: 0:00:00.139768
# -> 速くなってる；遅延評価後の値が保持されている