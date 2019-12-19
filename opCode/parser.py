def parse(data):
    return list(map(int, data.split(',')))



def loadPgm():
    with open('input', 'r') as f:
        pgm = parse(f.readline().strip())

    return pgm
