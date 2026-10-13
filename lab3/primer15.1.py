WeeksDayTranslation = dict()
WeeksDayTranslation['Monday'] = 'понедельник'
WeeksDayTranslation['Tuesday'] = 'вторник'
WeeksDayTranslation['Wednesday'] = 'среда'
Day = 'Monday'
if Day in WeeksDayTranslation:
    del WeeksDayTranslation[Day]

try:
    del WeeksDayTranslation[Day]
except KeyError:
    print(Day + ' нет в словаре')
print(WeeksDayTranslation)
