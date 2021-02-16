occupationList = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in occupationList:
    while ' ' in item:
        item = item[item.index(' ') + 1:]
    print(f'Привет, {item.capitalize()}')
