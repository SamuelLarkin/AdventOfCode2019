#!/usr/bin/env python3


from copy import deepcopy



def modes(op):
    """
    ABCDE
     1002

    DE - two-digit opcode,      02 == opcode 2
    C - mode of 1st parameter,  0 == position mode
    B - mode of 2nd parameter,  1 == immediate mode
    A - mode of 3rd parameter,  0 == position mode,
                                          omitted due to being a leading zero
    """
    opcode = op % 100
    mode1 = (op // 100) % 10
    mode2 = (op // 1000) % 10
    mode3 = (op // 10000) % 10
    assert mode3 == 0

    return opcode, mode1, mode2, mode3



def process(pgm, input_):
    pgm = deepcopy(pgm)
    instruction_pointer = 0
    response = 0xBAD
    while instruction_pointer < len(pgm):
        opcode, mode1, mode2, mode3 = modes(pgm[instruction_pointer])

        # Addition
        if opcode == 1:
            a = pgm[instruction_pointer+1]
            b = pgm[instruction_pointer+2]
            c = pgm[instruction_pointer+3]
            val_a = pgm[a] if mode1 == 0 else a
            val_b = pgm[b] if mode2 == 0 else b
            pgm[c] = val_a + val_b
            instruction_pointer += 4

        # Multiplication
        elif opcode == 2:
            a = pgm[instruction_pointer+1]
            b = pgm[instruction_pointer+2]
            c = pgm[instruction_pointer+3]
            val_a = pgm[a] if mode1 == 0 else a
            val_b = pgm[b] if mode2 == 0 else b
            pgm[c] = val_a * val_b
            instruction_pointer += 4

        # Opcode 3 takes a single integer as input and saves it to the position
        # given by its only parameter. For example, the instruction 3,50 would
        # take an input value and store it at address 50.
        elif opcode == 3:
            a = pgm[instruction_pointer+1]
            pgm[a] = input_
            instruction_pointer += 2

        # Opcode 4 outputs the value of its only parameter. For example, the
        # instruction 4,50 would output the value at address 50.
        elif opcode == 4:
            a = pgm[instruction_pointer+1]
            a = pgm[a] if mode1 == 0 else a
            response = a
            print(response)
            instruction_pointer += 2

        # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
        # the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing.
        elif opcode == 5:
            a = pgm[instruction_pointer+1]
            b = pgm[instruction_pointer+2]
            val_a = pgm[a] if mode1 == 0 else a
            val_b = pgm[b] if mode2 == 0 else b
            if val_a != 0:
                instruction_pointer = val_b
            else:
                instruction_pointer += 3

        # Opcode 6 is jump-if-false: if the first parameter is zero, it sets
        # the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing.
        elif opcode == 6:
            a = pgm[instruction_pointer+1]
            b = pgm[instruction_pointer+2]
            val_a = pgm[a] if mode1 == 0 else a
            val_b = pgm[b] if mode2 == 0 else b
            if val_a == 0:
                instruction_pointer = val_b
            else:
                instruction_pointer += 3

        # Opcode 7 is less than: if the first parameter is less than the second
        # parameter, it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        elif opcode == 7:
            a = pgm[instruction_pointer+1]
            b = pgm[instruction_pointer+2]
            c = pgm[instruction_pointer+3]
            val_a = pgm[a] if mode1 == 0 else a
            val_b = pgm[b] if mode2 == 0 else b
            pgm[c] = 1 if val_a < val_b else 0
            instruction_pointer += 4

        # Opcode 8 is equals: if the first parameter is equal to the second
        # parameter, it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        elif opcode == 8:
            a = pgm[instruction_pointer+1]
            b = pgm[instruction_pointer+2]
            c = pgm[instruction_pointer+3]
            val_a = pgm[a] if mode1 == 0 else a
            val_b = pgm[b] if mode2 == 0 else b
            pgm[c] = 1 if val_a == val_b else 0
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
        pgm = parse_input(f.readline())

    #print(_data)
    # Answer: 13346482
    print(process(pgm, 1))

    # Wrong: 223916824700594
    # Answer: 12111395
    print(process(pgm, 5))
