import sources.daily as daily
import sources.weekly as weekly

print('Daily forcast:', daily.forecast())
print('Weekly forecast:')
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

# import package.module
# module.attribute()
# >>> works
