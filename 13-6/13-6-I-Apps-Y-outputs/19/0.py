
import random

def solve(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split("+")
    
    # Initialize a set to store the distinct integers
    distinct_integers = set()
    
    # Iterate over the tokens
    for i in range(len(tokens)):
        # If the token is an integer, add it to the set of distinct integers
        if tokens[i].isdigit():
            distinct_integers.add(int(tokens[i]))
        # If the token is a plus symbol, randomly choose whether to interpret it as addition or string concatenation
        else:
            if random.randint(0, 1) == 0:
                # Interpret the plus symbol as addition
                distinct_integers.add(sum(distinct_integers))
            else:
                # Interpret the plus symbol as string concatenation
                distinct_integers.add(str(distinct_integers))
    
    # Return the number of distinct integers
    return len(distinct_integers)

