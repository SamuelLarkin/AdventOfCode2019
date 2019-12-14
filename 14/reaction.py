import math

from collections import Counter



def alll(desired_quantity, reaction):
    """
    """
    multiplier = int(math.ceil(float(desired_quantity) / reaction.quantity))
    r = Counter( { compound: multiplier * v for compound, v in reaction.reactants.items() } )
    r.update({ reaction.compound: -reaction.quantity })

    return r


def reaction_complete(reaction):
    """
    reaction: dict
    A reaction is complete when we are left with 'ORE' or that all reactants are negative.
    """
    return all( v < 0 for k, v in reaction.items() if k != 'ORE')



def react(reactions):
    fuel = Counter(reactions['FUEL'].reactants)
    while not reaction_complete(fuel):
        new_fuel = Counter(fuel)
        for compound, quantity in fuel.items():
            if compound == 'ORE' or quantity <= 0:
                continue
            new_fuel.update(alll(quantity, reactions[compound]))

        #fuel = Counter({ k: v for k, v in new_fuel.items() if v != 0 })
        # [How to: Remove zero and negative counts from a counter](https://kite.com/python/examples/686/collections-remove-zero-and-negative-counts-from-a-counter)
        fuel += Counter()

    return fuel
