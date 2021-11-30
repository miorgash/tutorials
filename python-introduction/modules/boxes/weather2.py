import sources

print('Daily forcast:', sources.daily.forecast())
print('Weekly forecast:')
for number, outlook in enumerate(sources.weekly.forecast(), 1):
    print(number, outlook)

# >>> import package
# works
# >>> package.module
# Traceback (most recent call last):
#   File "weather2.py", line 3, in <module>
#     print('Daily forcast:', sources.daily.forecast())
# AttributeError: module 'sources' has no attribute 'daily'
# パッケージをインポートはできるが、パッケージ内のモジュールは使えない
# import のあとは module として認識される
# package は module でもある？ので、 import package は可能
# package 以下の module を attribute として呼び出すことはできないのでエラー？
