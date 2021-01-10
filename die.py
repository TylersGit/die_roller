"""Functions that work with dice. 
Lets you roll many dice, save them to lists, roll standard
D&D stat arrays, and calculate damage averages."""

from random import randint

from helper_functions import *


def roll_die(times, size):
    """Lets you roll dice. 
    Size defines how many sides the die has.
    Times refers to how many times you roll that die.
    """
    
    rolls = [randint(1, size) for _time in range(times)]
    return rolls


def roll_stats():
    """Generates a standard D&D stat array, and prints the rolls formatted nicely."""
    stat_rolls = [roll_die(4, 6) for _state in range(6)]
    stat_array = sum_stats(stat_rolls)

    read_stats(stat_array)


def roll_average(times, size, iterations):
    """Rolls a set of dice multiple times, and calculates the average of all the rolls."""
    roll_totals = []

    for iteration in range(iterations):
        rolls = roll_die(times, size)
        roll_totals.append(sum(rolls))
    
    average = sum(roll_totals)/len(roll_totals)
    if iterations == 1:
        print(f"Rolling 1d{size} one time resulted in an " +
              f"average of {average}\n")
    else:
        print(f"Rolling {times}d{size} {iterations} times resulted in an " +
              f"average of {average}\n")
