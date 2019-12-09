#!/usr/bin/env  python3

from interpreter import Interpreter
from parser import parse




if __name__ == '__main__':
    with open('input', 'r') as f:
        pgm = parse(f.readline())

    interpreter = Interpreter(pgm)
    answer = interpreter(1)
    # Answer: 2351176124
    print('PartI:', answer)

    interpreter = Interpreter(pgm)
    answer = interpreter(2)
    # Answer: 2351176124
    print('PartII:', answer)
