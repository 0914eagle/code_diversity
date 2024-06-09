
import random

def solve(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split('+')
    
    # Initialize a set to store the distinct integers
    distinct_ints = set()
    
    # Iterate through each token in the list
    for token in tokens:
        # If the token is an integer, add it to the set of distinct integers
        if token.isdigit():
            distinct_ints.add(int(token))
        # If the token is a plus symbol, randomly choose whether to interpret it as addition or string concatenation
        else:
            if random.randint(0, 1) == 0:
                distinct_ints.add(str(distinct_ints.pop()) + token)
            else:
                distinct_ints.add(str(distinct_ints.pop()) + str(distinct_ints.pop()))
    
    # Return the number of distinct integers
    return len(distinct_ints)

