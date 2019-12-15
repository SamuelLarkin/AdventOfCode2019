#!/usr/bin/env  python3


from parser import parse
from reaction import react
from reaction import findMaximumYield




if __name__ == '__main__':
    with open('input', 'r') as f:
        reactions = parse(f.readlines())

    # Answer: 631171  too high
    # Answer: 628586
    print('PartI:', react(reactions))

    print('Part II:', findMaximumYield(reactions, ore_quantity=1000000000000))
