"""This program lets the user roll dice of different sizes, and do certain 
operations with them. such as rolling stats arrays, and calculating average of
spells damage."""

from die import *

# Lists the valid key options to choose from.
valid_keys = ['1', '2', ]

active = True

while active:
    print("Enter '1' for stat roller, enter '2' for average calculator.")
    print("Enter 'q' to quit. ")

    key = input()
    if key not in valid_keys:
        break
    elif key == '1':
        roll_stats()
    elif key == '2':
        inputs = average_get_inputs()
        roll_average(inputs['times'], inputs['size'], inputs['iterations'])
