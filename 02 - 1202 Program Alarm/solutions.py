#!/usr/bin/env python3


from copy import deepcopy



def parse(_input):
    return list(map(int, _input.split(',')))



def process(data):
    i=0
    while i < len(data):
        op = data[i]
        a = data[i+1]
        b = data[i+2]
        c = data[i+3]
        if op == 1:
            data[c] = data[a] + data[b]
        elif op == 2:
            data[c] = data[a] * data[b]
        elif op == 99:
            return data[0], data[1], data[2]
        else:
            raise Exception('Invalid op code')
        i += 4

    return None





if __name__ == '__main__':
    with open('input', 'r') as f:
        _data = parse(f.readline())

    data = deepcopy(_data)
    data[1] = 12
    data[2] = 2
    result, noun, verb = process(data)
    print(result)

    target = 19690720
    for a in range(100):
        data = deepcopy(_data)
        data[1] = a
        data[2] = 2
        result, noun, verb = process(data)
        if result > target:
            a -= 1
            break
    for b in range(100):
        data = deepcopy(_data)
        data[1] = a
        data[2] = b
        result, noun, verb = process(data)
        if result > target:
            b -= 1
            break

    print(a, b)
    data = deepcopy(_data)
    data[1] = 33
    data[2] = 76
    result, noun, verb = process(data)
    answer = 100 * noun + verb
    print(answer)
