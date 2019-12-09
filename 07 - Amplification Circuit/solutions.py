#!/usr/bin/env  python3

from opCode import amplify
from itertools import permutations
from tqdm import tqdm


def parse_input(input_str):
    return tuple(map(int, input_str.split(',')))






if __name__ == '__main__':
    with open('input', 'r') as f:
        pgm = parse_input(f.readline())

    answers = [ amplify(pgm, settings) for settings in tqdm(permutations(range(5), 5)) ]
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print('PartI:', answer)


    _input = 0
    answers = [ amplify(pgm, settings, _input) for settings in tqdm(permutations(range(5,10), 5)) ]
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print('PartII:', answer)
