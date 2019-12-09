from .interpreter import Interpreter



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
    """
    Amplifier first seen in day 07.
    """
    interpreters = [ Interpreter(pgm, initial_setting=setting) for setting in settings ]

    answers = []
    while _input is not None:
        for interpreter in interpreters:
            _input = interpreter(_input)
        answers.append(interpreters[-1].response)

    return answers[-1]
