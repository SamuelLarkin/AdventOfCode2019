#!/usr/bin/env python3

from pathlib import Path



def toTuple(value):
    values = list(map(int, str(value)))
    assert len(values) == 6
    return values



def twoDigits(values):
    assert len(values) == 6
    return any(a == b for a, b in zip(values, values[1:]))


def twoDigitsOnly(values):
    assert len(values) == 6
    return not any(a == b == c  for a, b, c in zip(values, values[1:], values[2:]))


def increasing(values):
    assert len(values) == 6
    #return values == tuple(sorted(values))
    return all(a <= b for a, b in zip(values, values[1:]))





if __name__ == '__main__':
    low, high = 235741, 706948

    print(toTuple(low))
    print('twoDigits')
    print(123446, twoDigits(toTuple(123446)))
    print(123789, twoDigits(toTuple(123789)))
    print('increasing')
    print(123446, increasing(toTuple(123446)))
    print(123441, increasing(toTuple(123441)))
    print(706948, increasing(toTuple(706948)))

    print(111111, list(filter(increasing, filter(twoDigits, map(toTuple, [111111])))))
    print(223450, list(filter(increasing, filter(twoDigits, map(toTuple, [223450])))))
    print(123789, list(filter(increasing, filter(twoDigits, map(toTuple, [123789])))))

    print(112233, list(filter(twoDigitsOnly, filter(increasing, filter(twoDigits, map(toTuple, [112233]))))))
    print(123444, list(filter(twoDigitsOnly, filter(increasing, filter(twoDigits, map(toTuple, [123444]))))))
    print(111122, list(filter(twoDigitsOnly, filter(increasing, filter(twoDigits, map(toTuple, [111122]))))))

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
 
    # answer 2:
    values = list(filter(twoDigitsOnly, values))
    print(*values, sep='\n')
    print(len(values))
