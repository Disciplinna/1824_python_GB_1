duration = int (input('Продолжительность в секундах: '))
minute = 60
hour = 3600
day = 86400
if duration<minute:
    print ('{} сек'.format(duration))
elif minute <= duration and hour > duration:
    minute = duration // 60 % 60
    second = duration % 60
    print ('{} мин {} сек'.format(minute,second));
elif duration >= hour and duration < day:
    day = duration // 86400
    hour = duration // 3600 % 24
    minute = duration // 60 % 60
    second = duration % 60
    print ('{} час {} мин {} сек'.format(hour,minute,second));
elif duration >= day:
    day = duration // 86400
    hour = duration // 3600 % 24
    minute = duration // 60 % 60
    second = duration % 60
    print('{} дн {} час {} мин {} сек'.format(day, hour, minute, second));
