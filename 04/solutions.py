#!/usr/bin/env python3

from collections import Counter
from pathlib import Path



def toTuple(value):
    values = tuple(map(int, str(value)))
    assert len(values) == 6
    return values



def twoDigits(values):
    assert len(values) == 6
    return any(a == b for a, b in zip(values, values[1:]))


def hasAPairOfDigits(values, invalid = set((3,5))):
    assert len(values) == 6
    #return len(invalid & set(Counter(values).values())) == 0
    c = Counter(values)
    return 2 in c.values()


def increasing(values):
    assert len(values) == 6
    #return values == tuple(sorted(values))
    return all(a <= b for a, b in zip(values, values[1:]))





if __name__ == '__main__':
    low, high = 235741, 706948

    answer1 = Path('answer1.txt')
    if not answer1.exists():
        values = list(filter(increasing, filter(twoDigits, map(toTuple, range(low, high+1)))))
        with answer1.open('w') as f:
            for value in values:
                print(*value, sep='', file=f)
    else:
        with answer1.open('r') as f:
            values = list(map(toTuple, map(str.strip, f.readlines())))

    # Answer 1: 1178
    assert len(values) < high - low + 1
    print(len(values))
 
    # answer 2: 763
    values = list(filter(hasAPairOfDigits, values))
    #print(*values, sep='\n')
    print(len(values))
