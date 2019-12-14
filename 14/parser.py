from collections import namedtuple


Reaction = namedtuple('Reaction', ('quantity', 'compound', 'reactants'))


def subparse(a):
    multiplier, compound = a.split()
    return int(multiplier), compound



def parse(iterable):
    reactions = {}
    for line in iterable:
        reactants, yield_ = line.split('=>')
        reactants = reactants.split(',')
        yield_ = subparse(yield_)
        reactants = { compound: multiplier for multiplier, compound in map(subparse, reactants) }
        reactions[yield_[1]] = Reaction(yield_[0], yield_[1], reactants)

    return reactions
