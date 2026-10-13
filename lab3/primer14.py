WeeksDayTranslation = dict()
WeeksDayTranslation['Monday'] = 'понедельник'
WeeksDayTranslation['Tuesday'] = 'вторник'
WeeksDayTranslation['Wednesday'] = 'среда'
WeeksDay = ['Monday', 'Tuesday', 'Wednesday']
for Day in WeeksDay:
    if Day in WeeksDayTranslation:
        print(Day + ' - это ' + WeeksDayTranslation[Day])
    else:
        print('Неизвестный день ' + Day)
