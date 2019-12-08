#!/usr/bin/env  python3

import opcodeInt

from functools import partial
from itertools import permutations
from multiprocessing import Process
from multiprocessing import Queue
from tqdm import tqdm



def amplify1(pgm, settings, _input = 0):
    queues = [ Queue() for _ in settings ]
    for queue, setting in zip(queues, settings):
        queue.put(setting)
    queues[0].put(_input)

    for i, _ in enumerate(settings):
        Process(target=opcodeInt.process, args=(pgm, queues[i], queues[(i+1)%5])).start()

    #response = queues[-1].get()
    response = [ queue.get() for queue in queues ]

    return response



def amplify(pgm, settings, _input = 0):
    interpreters = [ opcodeInt.OpCodeInterpreter(pgm) for _ in settings ]
    for interpreter, setting in zip(interpreters, settings):
        interpreter(setting)

    answers = []
    while _input is not None:
        for interpreter in interpreters:
            _input = interpreter(_input)
        answers.append(interpreters[-1].response)

    print(answers)







if __name__ == '__main__':
    pgm = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    amplify(pgm, (9,8,7,6,5))
    import sys
    sys.exit()

    with open('input', 'r') as f:
        pgm = opcodeInt.parse_input(f.readline())

    answers = [ amplify(pgm, settings) for settings in tqdm(permutations(range(5), 5)) ]
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print(answer)


    _input = 0
    answers = []
    for settings in tqdm(permutations(range(5,10), 5)):
        _input = amplify(pgm, settings, _input)
        answers.append(_input)
    answer = sorted(answers)[-1]

    print(answers)
    # Answer: 51679
    print(answer)
