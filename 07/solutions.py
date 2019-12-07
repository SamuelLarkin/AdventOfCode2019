#!/usr/bin/env  python3

import opcodeInt

from functools import partial
from itertools import permutations
from tqdm import tqdm


def amplify(pgm, settings, _input = 0):
    interpreter = partial(opcodeInt.process, pgm=pgm)
    for setting in settings:
        _input = interpreter(inputs=[_input, setting])

    return _input


if __name__ == '__main__':
    pgm = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    amplify(pgm, (9,8,7,6,5))

    with open('input', 'r') as f:
        pgm = opcodeInt.parse_input(f.readline())

    answers = [ amplify(pgm, settings) for settings in tqdm(permutations(range(5), 5)) ]
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print(answer)


    _input = 0
    answers = []
    for settings in tqdm(permutations(range(5,10), 5)):
        _input = amplify(pgm, settings, _input)
        answers.append(_input)
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print(answer)
