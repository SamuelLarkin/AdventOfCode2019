from collections import namedtuple


Reaction = namedtuple('Reaction', ('quantity', 'compound', 'reactants', 'distance'))


def subparse(a):
    quantity, compound = a.strip().split()
    return int(quantity), compound.strip()



def distance(compound, reactions):
    reaction = reactions[compound]
    if reaction.distance is None:
        reactants = reaction.reactants
        _distance = max( distance(c, reactions) for c in reaction.reactants ) + 1
        # Update our local copy then add it to the reactions.
        reaction = reaction._replace(distance = _distance)
        reactions[compound] = reaction

    return reaction.distance



def parse(iterable):
    """
    Read in the the reactions.
    """
    reactions = { 'ORE': Reaction(quantity=0, compound='ORE', distance=0, reactants={}) }
    for line in iterable:
        reactants, yield_ = line.split('=>')
        quantity, compound = subparse(yield_)
        reactants = { c: q for q, c in map(subparse, reactants.split(',')) }
        reactions[compound] = Reaction(quantity, compound, reactants, None)

    distance('FUEL', reactions)

    return reactions
