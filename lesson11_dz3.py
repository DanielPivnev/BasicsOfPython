class NotANumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def str_to_float(str_num):
    try:
        return float(str_num)
    except:
        raise NotANumber('Enter please the next time a just number.')

inputed_txt = ''
number_list = []
a = True
while a:
    try:
        inputed_txt = input('Enter please just a number which you want add to the list '
                                  'or if you are ready enter "stop": ')
        if inputed_txt == 'stop':
            a = False
        else:
            number_list.append(str_to_float(inputed_txt))
    except NotANumber as e:
        print(e)
print(f'Here are your list of numbers: {number_list} \nThank you! Jesus love you!')
