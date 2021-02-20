import random


def get_jocks(jocks_number=1, reaped_jocks_words=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jocks_list = []
    if reaped_jocks_words == True:
        while jocks_number >= 1:
            jocks_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            jocks_number -= 1
    elif reaped_jocks_words == False:
        n_num = list(random.sample(nouns, jocks_number))
        adv_num = list(random.sample(adverbs, jocks_number))
        adj_num = list(random.sample(adjectives, jocks_number))
        for n, adv, adj in zip(n_num, adv_num, adj_num):
            jocks_list.append(f'{n} {adv} {adj}')
    return list(jocks_list)


print(get_jocks(3, True))
