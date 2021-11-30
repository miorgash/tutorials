from pprint import pprint
import sys
import os
pprint(sys.path)

from sources import daily, weekly

print('Daily forcast:', daily.forecast())
print('Weekly forecast:')
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

# >>> from package import module
# >>> module.attribute()
# works