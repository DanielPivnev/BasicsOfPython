


def currency_rates(code):
    from requests import get, utils
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encode = utils.get_encoding_from_headers(response.headers)
    cont = response.content.decode(encoding=encode)
    cont = cont.replace('/', '')
    cont = cont.split('<Valute>')
    land1 = 'BYN'
    for i in range(1, len(cont) - 1):
        cont[i] = cont[i].split('CharCode')
        cont[i][1] = cont[i][1].replace('>', '',).replace('<', '')
        cont[i][2] = cont[i][2].split('<Value>')
        cont[i][2] = cont[i][2][1:2]
        cont[i][2][0] = cont[i][2][0].replace(',', '.')
        if cont[i][1] == land1:
            land1 = cont[i][2][0]
    for i in range(1, len(cont)):
        if cont[i][1] == code.upper():
            land2 = cont[i][2][0]
            return print(f'{cont[i][1]} = {cont[i][2][0]} \nОдин Белорусский рубль это {float(land1) / float(land2):0.2f} {cont[i][1]}')

