
import random

def solve(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split('+')
    
    # Initialize a set to store the distinct integers
    distinct_ints = set()
    
    # Iterate over the tokens
    for i in range(len(tokens)):
        # If the token is an integer, add it to the set
        if tokens[i].isdigit():
            distinct_ints.add(int(tokens[i]))
        # If the token is a plus symbol, randomly choose whether to interpret it as addition or string concatenation
        else:
            if random.randint(0, 1) == 0:
                # Interpret it as addition
                distinct_ints.add(int(tokens[i-1]) + int(tokens[i+1]))
            else:
                # Interpret it as string concatenation
                distinct_ints.add(int(tokens[i-1]) * int(tokens[i+1]))
    
    # Return the number of distinct integers
    return len(distinct_ints)

