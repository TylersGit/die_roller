"""This program lets the user roll dice of different sizes, and do certain 
operations with them. such as rolling stats arrays, and calculating avarage of 
spells damage."""

from die import *

die_times_prompt = "How many dice would you like to roll? "
die_size_prompt = "What size of die would you like to roll? "
die_iter_prompt = "How many iterations would you like to roll? "


active = True

while active:
    print("Enter '1' for stat roller, enter '2' for avarage calculator.")
    print("Enter 'q' to quit. ")
    
    key = input()
    if key == 'q':
        break
    elif key == '1':
        print("Did you get here?")
    elif key == '2':
        # Asks for the inputs required for the roll_average() method.
        size = int(input(die_size_prompt))
        times = int(input(die_times_prompt))
        iterations = int(input(die_iter_prompt))

        
        average = roll_average(size, times, iterations)
        print(f"Rolling {times}d{size} {iterations} times resulted in an " +
              f"average of {average}\n")