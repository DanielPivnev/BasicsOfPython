listOfQuebes = []
SumOfQuebesDivideSeven = 0

i = 0
while i <= 1000:
    listOfQuebes.append(i**3)
    quebe = listOfQuebes[i]
    sum = 0
    while quebe != 0:
        sum += quebe % 10
        quebe = int(quebe / 10)
    if sum % 7 == 0:
        SumOfQuebesDivideSeven += listOfQuebes[i]
    i += 1

print('a)', SumOfQuebesDivideSeven)

i = 0
while i <= 1000:
    listOfQuebes.append(i**3 + 17)
    quebe = listOfQuebes[i]
    sum = 0
    while quebe != 0:
        sum += quebe % 10
        quebe = int(quebe / 10)
    if sum % 7 == 0:
        SumOfQuebesDivideSeven += listOfQuebes[i]
    i += 1
