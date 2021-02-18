sentenceList = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in sentenceList:
    if item == sentenceList[1] or item == sentenceList[3]:
        sentenceList[sentenceList.index(item)] = f'"{int(item):02d}"'
    elif item == sentenceList[-2]:
        sentenceList[sentenceList.index(item)] = f'"+{int(item):02d}"'

print(' '.join(sentenceList))