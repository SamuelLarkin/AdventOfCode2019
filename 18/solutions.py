#!/usr/bin/env  python3

import tunnel



def partI():
    with open('input', 'r') as f:
        answer = tunnel.partI(f)
    print('PartI:', answer)




if __name__ == '__main__':
    partI()
