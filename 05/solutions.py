#!/usr/bin/env python3


from copy import deepcopy



def process(data, input_):
    op_index = 0
    while op_index < len(data):
        op = data[op_index]
        mode1 = (op // 100) % 10
        mode2 = (op // 1000) % 10
        mode3 = (op // 10000) % 10
        opcode = op % 100
        assert mode3 == 0

        if opcode == 1:
            a = data[op_index+1]
            b = data[op_index+2]
            c = data[op_index+3]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            data[c] = val_a + val_b
            op_index += 4
        elif opcode == 2:
            a = data[op_index+1]
            b = data[op_index+2]
            c = data[op_index+3]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            data[c] = val_a * val_b
            op_index += 4
        elif opcode == 3:
            a = data[op_index+1]
            data[a] = input_
            op_index += 2
        elif opcode == 4:
            a = data[op_index+1]
            val = data[a]
            print(val)
            op_index += 2
        elif opcode == 99:
            return data[0], data[1], data[2]
        else:
            raise Exception(f'Invalid opcode code {opcode}{op}')

    return None





if __name__ == '__main__':
    with open('input', 'r') as f:
        _data = list(map(int, f.readline().split(',')))

    print(_data)
    process(_data, 1)
