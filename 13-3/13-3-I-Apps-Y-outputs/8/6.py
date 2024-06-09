
import random

def evaluate_expression(expression):
    tokens = expression.split("+")
    integers = [int(token) for token in tokens if token.isdigit()]
    plus_symbols = [token for token in tokens if token != ""]

    # Initialize a list to store the evaluated integers
    evaluated_integers = []

    # Loop through each plus symbol and randomly choose whether to evaluate it as addition or string concatenation
    for i in range(len(plus_symbols)):
        if random.randint(0, 1) == 0:
            # Evaluate the plus symbol as addition
            evaluated_integers.append(integers[i] + integers[i+1])
        else:
            # Evaluate the plus symbol as string concatenation
            evaluated_integers.append(str(integers[i]) + str(integers[i+1]))

    # Return the number of distinct integers in the evaluated list
    return len(set(evaluated_integers))

