durationS = int(input('Ведите пожалуйста время в секундах:'))
durationMin = 0
durationHour = 0
durationDay = 0
score = 0

if durationS > 59:
    durationMin = durationS // 60
    durationS -= durationMin * 60
    score += 1
    if durationMin > 59:
        score += 1
if score == 2:
    durationHour = durationMin // 60
    durationMin -= durationHour * 60
    if durationHour > 23:
        score += 1
if score == 3:
    durationDay = durationHour // 24
    durationHour -= durationDay * 24
    score += 1

if score == 0:
    print(durationS, 's')
elif score == 1:
    print(durationMin, 'min', durationS, 's')
elif score == 2:
    print(durationHour, 'hour', durationMin, 'min', durationS, 's')
else:
    print(durationDay, 'day', durationHour, 'hour', durationMin, 'min', durationS, 's')