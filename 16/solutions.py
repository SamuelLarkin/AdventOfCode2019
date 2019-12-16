#!/usr/bin/env  python3

from fft import fft



def partI(data):
    message = fft(data)
    answer = message[:8]
    print('Part I:', answer)
    assert answer == '29795507'

    return message





if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.readline()

    message = partI(data)

    offset = int(data[:7])
