def num_translate_adj(num):
    english_num = ('own', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'then')
    russian_num = ('один', 'два', 'три', 'читыре', 'пять', 'шесть', 'семь', 'восимь', 'девять', 'десять')
    for rus_num, eng_num in zip(russian_num, english_num):
        if num == rus_num:
            return str(eng_num)
        elif num == eng_num:
            return str(rus_num)
        elif num == rus_num.title():
            return str(eng_num.title())
        elif num == eng_num.title():
            return str(rus_num.title())
    return None


user_entered_num = input()

print(num_translate_adj(user_entered_num))
