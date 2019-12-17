#!/usr/bin/env  python3

import fft



def partI(data):
    message = fft.fft(data)
    answer = message[:8]
    print('Part I:', answer)
    assert answer == '29795507'



def partII(message):
    answer = fft.partII(message)
    print('Part II:', answer)
    assert answer == '89568529'





if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.readline().strip()

    if False:
        partI(data)

    if True:
        partII(data)
