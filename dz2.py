import yaml
import os


with open('config.yaml') as f:
    dicti = yaml.safe_load(f)
    for k, v in dicti.items():
        os.mkdir(k)
        for key, value in v.items():
            os.makedirs(os.path.join(k, key))
            i = len(value) - 1
            while i >= 0:
                if value[i] == f'{value[i]}':
                    open(os.path.join(os.path.join(k, key), value[i]), 'w', encoding='utf-8')
                else:
                    for k2, v2 in value[i].items():
                        os.makedirs(os.path.join(os.path.join(k, key), k2))
                        if v2 == f'{v2}':
                            for j in range(len(v2)):
                                open(os.path.join(os.path.join(os.path.join(k, key), k2), v2[j]), 'w', encoding='utf-8')
                        else:
                            for k3, v3 in v2.items():
                                os.makedirs(os.path.join(os.path.join(os.path.join(k, key), k2), k3))
                                for k4 in v3:
                                    open(os.path.join(os.path.join(os.path.join(os.path.join(k, key), k2), k3), k4), 'w', encoding='utf-8')
                i -= 1
