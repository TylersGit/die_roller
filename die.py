"""Functions that work with dice. 
Lets you roll many dice, save them to lists, roll standard
D&D stat arrays, and calculate damage averages."""

from random import randint

def roll_die(size, times, iterations):
    """Lets you roll dice. 
    Size defines how many sides the die has.
    Times refers to how many times you roll that die.
    """
    
    rolls = [randint(1, size) for time in range(times)]
    return rolls


def roll_stats():
    pass

def roll_average(size, times, iterations):
    roll_totals = []
    
    for iteration in range(iterations):
        rolls = roll_die(size, times)
        roll_totals.append(sum(rolls))
    
    average = sum(roll_totals)/len(roll_totals)
    return average