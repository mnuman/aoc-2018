def readfile(fname):
    with open(fname, 'r') as src:
        all_lines = src.readlines()
    y = 0
    track = []
    cars = {}
    for l in all_lines:
        l = l.strip('\n')
        if 'v' in l:
            dy, dx = 1, 0
            x = l.index('v')
            addline = l.replace('v', '|')
            cars[len(cars)] = y, x, dy, dx
        elif '^' in l:
            dy, dx = -1, 0
            x = l.index('^')
            addline = l.replace('^', '|')
            cars[len(cars)] = y, x, dy, dx
        elif '>' in l:
            dy, dx = 0, 1
            x = l.index('>')
            addline = l.replace('>', '-')
            cars[len(cars)] = y, x, dy, dx
        elif '<' in l:
            dy, dx = 0, -1
            x = l.index('<')
            addline = l.replace('<', '-')
            cars[len(cars)] = y, x, dy, dx
        else:
            addline = l
        track.append(addline)
        y += 1
    return (track, cars)


t, c = readfile('data/day13-test.txt')
print(c)
print(t)
