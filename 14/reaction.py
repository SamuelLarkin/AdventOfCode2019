import math

from collections import Counter



def substitution(desired_quantity, reaction):
    """
    """
    multiplier = int(math.ceil(float(desired_quantity) / reaction.quantity))
    r = Counter( { compound: multiplier * v for compound, v in reaction.reactants.items() } )
    r.update({ reaction.compound: -reaction.quantity * multiplier })

    return r


def reaction_complete(reaction):
    """
    reaction: dict
    A reaction is complete when we are left with 'ORE' or that all reactants are negative.
    """
    return all( v < 0 for k, v in reaction.items() if k != 'ORE')



def react(reactions):
    """
    Return the required 'ORE' to process the reactions.
    """
    fuel = Counter(reactions['FUEL'].reactants)  # {'A': 7, 'E': 1}
    while not reaction_complete(fuel):
        new_fuel = Counter(fuel)
        compound = sorted(fuel.keys(), key=lambda k: reactions[k].distance, reverse=True)[0]
        if compound == 'ORE':
            continue
        quantity = fuel[compound]
        new_fuel.update(substitution(quantity, reactions[compound]))

        #fuel = Counter({ k: v for k, v in new_fuel.items() if v != 0 })
        # [How to: Remove zero and negative counts from a counter](https://kite.com/python/examples/686/collections-remove-zero-and-negative-counts-from-a-counter)
        fuel = new_fuel + Counter()

    return fuel['ORE']
