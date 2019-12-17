import numpy as np
import typing

from itertools import chain
from itertools import cycle
from itertools import islice
from itertools import repeat
from tqdm import trange



def consume(iterator, n=None):
    """
    Advance the iterator n-steps ahead. If n is None, consume entirely.
    [Python itertools - cookbook](https://docs.python.org/3/library/itertools.html)
    """
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)



def coefficient_generator2(i:int):
    assert i > 0
    base = (0, 1, 0, -1)
    #return islice(repeat(chain.from_iterable(repeat(v, i) for v in base)), 1)
    pattern = chain.from_iterable(repeat(repeat(v, i) for v in base))
    for c in pattern:
        print(c)
    print(pattern)
    yield from islice(pattern, 1)



def coefficient_generator(i:int):
    assert i > 0
    base = (0, 1, 0, -1)
    while True:
        yield from chain.from_iterable(repeat(v, i) for v in base)



def coefficient(num:int, i:int):
    assert num > 0
    assert i > 0
    coefficient = iter(coefficient_generator(i))
    # Skip the first coefficient.
    next(coefficient)
    return [ next(coefficient)  for _ in range(num) ]



def fft(data, num_phases:int = 100):
    if isinstance(data, str):
        data = tuple(data.strip())
    data = np.array(data, dtype=np.int16).T
    num = data.shape[0]
    coeff = np.array([ coefficient(num, i) for i in range(1, num+1) ], dtype=np.int16)

    for _ in range(num_phases):
        data = np.mod(np.absolute(np.sum(np.multiply(data, coeff), axis=1)), 10)

    return ''.join(map(str, data.tolist()))



def partII(message):
    offset = int(message[:7])
    message = [ int(x) for x in message ]
    v = (10000*message)[offset:] # tail for part2
    for _ in trange(100):
        for i in trange(len(v)-1,0,-1): # need to do calculations from the end!!! that's the key idea!
            v[i-1] = (v[i-1] + v[i]) % 10

    return ''.join(map(str, v[:8]))
