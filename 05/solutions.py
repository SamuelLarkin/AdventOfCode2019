#!/usr/bin/env python3


from copy import deepcopy



def process(data, input_):
    instruction_pointer = 0
    response = 0xBAD
    while instruction_pointer < len(data):
        op = data[instruction_pointer]
        mode1 = (op // 100) % 10
        mode2 = (op // 1000) % 10
        mode3 = (op // 10000) % 10
        opcode = op % 100
        assert mode3 == 0

        if opcode == 1:
            a = data[instruction_pointer+1]
            b = data[instruction_pointer+2]
            c = data[instruction_pointer+3]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            data[c] = val_a + val_b
            instruction_pointer += 4
        elif opcode == 2:
            a = data[instruction_pointer+1]
            b = data[instruction_pointer+2]
            c = data[instruction_pointer+3]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            data[c] = val_a * val_b
            instruction_pointer += 4
        elif opcode == 3:
            a = data[instruction_pointer+1]
            data[a] = input_
            instruction_pointer += 2
        elif opcode == 4:
            a = data[instruction_pointer+1]
            response = data[a]
            print(response)
            instruction_pointer += 2
        elif opcode == 5:
            a = data[instruction_pointer+1]
            b = data[instruction_pointer+2]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            if val_a != 0:
                instruction_pointer = val_b
            else:
                instruction_pointer += 3
        elif opcode == 6:
            a = data[instruction_pointer+1]
            b = data[instruction_pointer+2]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            if val_a == 0:
                instruction_pointer = val_b
            else:
                instruction_pointer += 3
        elif opcode == 7:
            a = data[instruction_pointer+1]
            b = data[instruction_pointer+2]
            c = data[instruction_pointer+3]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            data[c] = 1 if val_a < val_b else 0
            instruction_pointer += 4
        elif opcode == 8:
            a = data[instruction_pointer+1]
            b = data[instruction_pointer+2]
            c = data[instruction_pointer+3]
            val_a = data[a] if mode1 == 0 else a
            val_b = data[b] if mode2 == 0 else b
            data[c] = 1 if val_a == val_b else 0
            instruction_pointer += 4
        elif opcode == 99:
            return response
        else:
            raise Exception(f'Invalid opcode code {opcode}{op}')

    return None


def parse_input(input_str):
    return list(map(int, input_str.split(',')))





if __name__ == '__main__':
    with open('input', 'r') as f:
        _data = list(map(int, f.readline().split(',')))

    #print(_data)
    # Answer: 13346482
    print(process(_data, 1))

    test = parse_input('3,9,8,9,10,9,4,9,99,-1,8')
    assert process(test, 7) == 0
    assert process(test, 8) == 1
    assert process(test, 9) == 0
    test = parse_input('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
    assert process(test, 0) == 0
    assert process(test, 1) == 1
    assert process(test, 2) == 1
    test = parse_input('3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
    assert process(test, 0) == 0
    assert process(test, 1) == 1
    assert process(test, 2) == 1

    # Wrong: 223916824700594
    print(process(_data, 5))
