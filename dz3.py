with open('users.csv', 'r', encoding='utf-8') as f_users:
    with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        dictUsers1 = {}
        user = f_users.readline()
        hobby = f_hobby.readline()
        while user and hobby:
            dictUsers2 = {}
            if hobby and user:
                dictUsers2.setdefault(user.replace(',', ' ').replace('\n', ''), hobby.replace(',', ', ').replace('\n', ''))
            elif hobby and not user:
                dictUsers2.setdefault(None, hobby)
            else:
                break
            dictUsers1.update(dictUsers2)
            user = f_users.readline()
            hobby = f_hobby.readline()
print(dictUsers1)
