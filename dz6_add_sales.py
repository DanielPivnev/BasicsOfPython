from sys import argv


with open('backary.scv', 'a') as f:
    way, args = argv
    f.writelines(args)
    f.write('\n')
