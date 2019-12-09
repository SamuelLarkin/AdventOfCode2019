#!/usr/bin/env python3



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



class Interpreter:
    def __init__(self, pgm, initial_setting = None):
        self.pgm = list(pgm)  # Effectively making a deepcopy from readonly to write-enabled memory.
        self.instruction_pointer = 0
        self.response = 0xBAD
        if initial_setting is not None:
            opcode, mode1, mode2, mode3 = modes(self.pgm[self.instruction_pointer])
            # Opcode 3 takes a single integer as input and saves it to the position
            # given by its only parameter. For example, the instruction 3,50 would
            # take an input value and store it at address 50.
            if opcode == 3:
                a = self.pgm[self.instruction_pointer+1]
                self.pgm[a] = initial_setting
                self.instruction_pointer += 2
            else:
                assert False, 'Can only initialize if the first instruction is a read opcode.'


    def __call__(self, input_):
        if input_ is None:
            return None

        while self.instruction_pointer < len(self.pgm):
            opcode, mode1, mode2, mode3 = modes(self.pgm[self.instruction_pointer])

            # Addition
            if opcode == 1:
                a = self.pgm[self.instruction_pointer+1]
                b = self.pgm[self.instruction_pointer+2]
                c = self.pgm[self.instruction_pointer+3]
                val_a = self.pgm[a] if mode1 == 0 else a
                val_b = self.pgm[b] if mode2 == 0 else b
                self.pgm[c] = val_a + val_b
                self.instruction_pointer += 4

            # Multiplication
            elif opcode == 2:
                a = self.pgm[self.instruction_pointer+1]
                b = self.pgm[self.instruction_pointer+2]
                c = self.pgm[self.instruction_pointer+3]
                val_a = self.pgm[a] if mode1 == 0 else a
                val_b = self.pgm[b] if mode2 == 0 else b
                self.pgm[c] = val_a * val_b
                self.instruction_pointer += 4

            # Opcode 3 takes a single integer as input and saves it to the position
            # given by its only parameter. For example, the instruction 3,50 would
            # take an input value and store it at address 50.
            elif opcode == 3:
                a = self.pgm[self.instruction_pointer+1]
                self.pgm[a] = input_
                self.instruction_pointer += 2

            # Opcode 4 outputs the value of its only parameter. For example, the
            # instruction 4,50 would output the value at address 50.
            elif opcode == 4:
                a = self.pgm[self.instruction_pointer+1]
                a = self.pgm[a] if mode1 == 0 else a
                self.response = a
                self.instruction_pointer += 2
                return self.response

            # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
            # the instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            elif opcode == 5:
                a = self.pgm[self.instruction_pointer+1]
                b = self.pgm[self.instruction_pointer+2]
                val_a = self.pgm[a] if mode1 == 0 else a
                val_b = self.pgm[b] if mode2 == 0 else b
                if val_a != 0:
                    self.instruction_pointer = val_b
                else:
                    self.instruction_pointer += 3

            # Opcode 6 is jump-if-false: if the first parameter is zero, it sets
            # the instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            elif opcode == 6:
                a = self.pgm[self.instruction_pointer+1]
                b = self.pgm[self.instruction_pointer+2]
                val_a = self.pgm[a] if mode1 == 0 else a
                val_b = self.pgm[b] if mode2 == 0 else b
                if val_a == 0:
                    self.instruction_pointer = val_b
                else:
                    self.instruction_pointer += 3

            # Opcode 7 is less than: if the first parameter is less than the second
            # parameter, it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            elif opcode == 7:
                a = self.pgm[self.instruction_pointer+1]
                b = self.pgm[self.instruction_pointer+2]
                c = self.pgm[self.instruction_pointer+3]
                val_a = self.pgm[a] if mode1 == 0 else a
                val_b = self.pgm[b] if mode2 == 0 else b
                self.pgm[c] = 1 if val_a < val_b else 0
                self.instruction_pointer += 4

            # Opcode 8 is equals: if the first parameter is equal to the second
            # parameter, it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            elif opcode == 8:
                a = self.pgm[self.instruction_pointer+1]
                b = self.pgm[self.instruction_pointer+2]
                c = self.pgm[self.instruction_pointer+3]
                val_a = self.pgm[a] if mode1 == 0 else a
                val_b = self.pgm[b] if mode2 == 0 else b
                self.pgm[c] = 1 if val_a == val_b else 0
                self.instruction_pointer += 4

            elif opcode == 99:
                return None

            else:
                raise Exception(f'Invalid opcode code {opcode}{op}')

        return None
