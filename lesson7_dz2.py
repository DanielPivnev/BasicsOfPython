import os


my_project = input('Enter please the name of your project: ')
os.mkdir(my_project)
dirs1 = []
dirs2 = []
dirs3 = []
path_dir = os.path.join(my_project, r'')


def create_dir(path, dirict):
    try:
        txt1 = input(f'Enter please the name of your directory in {dirict} else put "enter": ')
        os.makedirs(os.path.join(path, txt1))
        return txt1
    except:
        return str('ready')


def create_file(path, dirict):
    try:
        txt1 = input(f'Enter please the name of your a file in {dirict} else enter "ready": ')
        open(os.path.join(path, txt1), 'x', encoding='utf-8')
    except:
        return str('ready')


while 1:
    txt = create_dir(path_dir, my_project)
    if txt == 'ready':
        break
    dirs1.append(txt)

for dirict1 in dirs1:
    path_dir1 = os.path.join(path_dir, dirict1)
    dirs2 = []
    dirs3 = []
    while 1:
        txt = create_dir(path_dir1, dirict1)
        if txt == 'ready':
            break
        dirs2.append(txt)
    while 1:
        txt = create_file(path_dir1, dirict1)
        if txt == 'ready':
            break

    for dirict2 in dirs2:
        dirs3 = []
        path_dir2 = os.path.join(path_dir1, dirict2)
        while 1:
            txt = create_dir(path_dir2, dirict2)
            if txt == 'ready':
                break
            dirs3.append(txt)
        while 1:
            txt = create_file(path_dir2, dirict2)
            if txt == 'ready':
                break

        for dirict3 in dirs3:
            path_dir3 = os.path.join(path_dir2, dirict3)
            while 1:
                txt = create_dir(path_dir3, dirict3)
                if txt == 'ready':
                    break
            while 1:
                txt = create_file(path_dir3, dirict3)
                if txt == 'ready':
                    break
