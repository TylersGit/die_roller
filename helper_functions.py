"""Module with helper funtions for die.py and die_roller.py
All the clutter will be here so the other files could be 
more readable."""

def read_stats(stat_array):
    """Prints the stats rolled in a neat format."""
    for _stat in stat_array:
        print(f"You rolled a {_stat}")
    print('\n')

def sum_stats(stat_rolls):
    stat_array = []

    for _stat in stat_rolls:
        _stat.sort()
        del _stat[0]
        stat_array.append(sum(_stat))
    
    return stat_array

def average_get_inputs():
    """Asks for the inputs required for the roll_average() method."""
    size = int(input(die_size_prompt))
    times = int(input(die_times_prompt))
    iterations = int(input(die_iter_prompt))

    return {
        'size': size,
        'times': times,
        'iterations': iterations
    }


# Prompts for the roll_average in die_roller.py
die_times_prompt = "How many dice would you like to roll? "
die_size_prompt = "What size of die would you like to roll? "
die_iter_prompt = "How many iterations would you like to roll? "
