def t(*args):
    dict1 = {}

    for name in args:
        dict1_key = name[name.index(' ') + 1]
        dict1.setdefault(dict1_key)
        dict2 = {}
        for first_name in args:
            dict2_key = first_name[0]
            list_names = []
            for full_name in args:
                if full_name[full_name.index(' ') + 1] == dict1_key and full_name[0] == dict2_key:
                    list_names.append(full_name)
            if first_name[first_name.index(' ') + 1] == dict1_key:
                dict2.setdefault(dict2_key)
                dict2[dict2_key] = list_names
                dict1[dict1_key] = dict2
    return dict1


tt = t()

print(t("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
