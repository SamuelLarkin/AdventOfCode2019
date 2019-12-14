#!/usr/bin/env python3

from enum import IntEnum



class opCodeType(IntEnum):
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUAL = 8
    BASE = 9
    DONE = 99



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
    #assert mode3 == 0, f'mode3 {mode3}'

    return opCodeType(opcode), mode1, mode2, mode3



class Interpreter:
    def __init__(self, pgm, inp):
        self.pgm = list(pgm) + [-1]*10000000  # Effectively making a deepcopy from readonly to write-enabled memory.
        self.instruction_pointer = 0
        self.relative_base = 0
        self.input = iter(inp)


    def getInArg(self, offset, mode):
        a = self.pgm[self.instruction_pointer+offset]
        if mode == 0:
            return self.pgm[a]
        elif mode == 1:
            return a
        elif mode == 2:
            return self.pgm[self.relative_base + a]
        else:
            assert False, 'Unsupported mode'


    def getOutArg(self, offset, mode):
        a = self.pgm[self.instruction_pointer+offset]
        if mode == 0:
            return a
        elif mode == 1:
            return a
        elif mode == 2:
            return self.relative_base + a
        else:
            assert False, 'Unsupported mode'


    # NOT __next__
    def __iter__(self):
        while self.instruction_pointer < len(self.pgm):
            opcode, mode1, mode2, mode3 = modes(self.pgm[self.instruction_pointer])

            # Addition
            if opcode == opCodeType.ADD:
                val_a = self.getInArg(1, mode1)
                val_b = self.getInArg(2, mode2)
                self.pgm[self.getOutArg(3, mode3)] = val_a + val_b
                self.instruction_pointer += 4

            # Multiplication
            elif opcode == opCodeType.MUL:
                val_a = self.getInArg(1, mode1)
                val_b = self.getInArg(2, mode2)
                self.pgm[self.getOutArg(3, mode3)] = val_a * val_b
                self.instruction_pointer += 4

            # Opcode 3 takes a single integer as input and saves it to the position
            # given by its only parameter. For example, the instruction 3,50 would
            # take an input value and store it at address 50.
            elif opcode == opCodeType.INPUT:
                self.pgm[self.getOutArg(1, mode1)] = next(self.input)
                self.instruction_pointer += 2

            # Opcode 4 outputs the value of its only parameter. For example, the
            # instruction 4,50 would output the value at address 50.
            elif opcode == opCodeType.OUTPUT:
                val_a = self.getInArg(1, mode1)
                self.instruction_pointer += 2
                yield val_a

            # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
            # the instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            elif opcode == opCodeType.JUMP_IF_TRUE:
                val_a = self.getInArg(1, mode1)
                val_b = self.getInArg(2, mode2)
                if val_a != 0:
                    self.instruction_pointer = val_b
                else:
                    self.instruction_pointer += 3

            # Opcode 6 is jump-if-false: if the first parameter is zero, it sets
            # the instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            elif opcode == opCodeType.JUMP_IF_FALSE:
                val_a = self.getInArg(1, mode1)
                val_b = self.getInArg(2, mode2)
                if val_a == 0:
                    self.instruction_pointer = val_b
                else:
                    self.instruction_pointer += 3

            # Opcode 7 is less than: if the first parameter is less than the second
            # parameter, it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            elif opcode == opCodeType.LESS_THAN:
                val_a = self.getInArg(1, mode1)
                val_b = self.getInArg(2, mode2)
                self.pgm[self.getOutArg(3, mode3)] = 1 if val_a < val_b else 0
                self.instruction_pointer += 4

            # Opcode 8 is equals: if the first parameter is equal to the second
            # parameter, it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            elif opcode == opCodeType.EQUAL:
                val_a = self.getInArg(1, mode1)
                val_b = self.getInArg(2, mode2)
                self.pgm[self.getOutArg(3, mode3)] = 1 if val_a == val_b else 0
                self.instruction_pointer += 4

            # adjusts the relative base by the value of its only parameter. The
            # relative base increases (or decreases, if the value is negative)
            # by the value of the parameter.
            elif opcode == opCodeType.BASE:
                val_a = self.getInArg(1, mode1)
                self.relative_base += val_a
                self.instruction_pointer += 2

            elif opcode == opCodeType.DONE:
                break

            else:
                raise Exception(f'Invalid opcode code {opcode}')
