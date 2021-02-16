sentenceList = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in sentenceList:
    if item == '5' or item == '17':
        sentenceList[sentenceList.index(item)] = f'"{int(item):02d}"'
    elif item == '+5':
        sentenceList[sentenceList.index(item)] = f'"+{int(item):02d}"'

print(' '.join(sentenceList))