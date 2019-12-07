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
    with open('input', 'r') as f:
        pgm = opcodeInt.parse_input(f.readline())

    answers = [ amplify(pgm, settings) for settings in tqdm(permutations(range(5), 5)) ]
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print(answer)
