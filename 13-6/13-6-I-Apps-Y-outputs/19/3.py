
import random

def solve(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split('+')
    
    # Initialize a set to store the distinct integers
    distinct_integers = set()
    
    # Loop through each token in the list
    for i in range(len(tokens)):
        # If the token is an integer, add it to the set of distinct integers
        if tokens[i].isdigit():
            distinct_integers.add(int(tokens[i]))
        # If the token is a plus symbol, choose a random integer to concatenate with the previous integer
        else:
            # Get the previous integer
            prev_integer = int(tokens[i-1])
            # Get a random integer to concatenate with the previous integer
            rand_integer = random.randint(0, 9)
            # Concatenate the previous integer with the random integer
            concat_integer = str(prev_integer) + str(rand_integer)
            # Add the concatenated integer to the set of distinct integers
            distinct_integers.add(int(concat_integer))
    
    # Return the number of distinct integers
    return len(distinct_integers)

