from sys import argv

with open('backary.scv', 'r') as f:
    try:
        way, lines = argv
        lines = int(lines)
        i = 1
        while i < lines:
            _ = f.readline()
            i += 1
        line = f.readline().strip()
        while line:
            print(line)
            line = f.readline().strip()
    except:
        try:
            way, from_lines, to_lines = argv
            from_lines = int(from_lines)
            to_lines = int(to_lines)
            i = 1
            j = 1
            while i <= to_lines:
                while j < from_lines:
                    _ = f.readline()
                    j += 1
                    i += 1
                line = f.readline().strip()
                print(line)
                i += 1
        except:
            line = f.readline().strip()
            while line:
                print(line)
                line = f.readline().strip()
