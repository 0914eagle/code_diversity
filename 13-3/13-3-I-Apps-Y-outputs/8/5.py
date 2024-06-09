
import random

def evaluate_expression(expression):
    tokens = expression.split("+")
    integers = [int(token) for token in tokens if token.isdigit()]
    plus_symbols = ["+" for token in tokens if token != ""]
    total_combinations = 1
    for i in range(len(plus_symbols)):
        if random.randint(0, 1) == 0:
            total_combinations *= len(integers)
        else:
            total_combinations *= len(plus_symbols)
    return total_combinations

if __name__ == "__main__":
    expression = input()
    print(evaluate_expression(expression))

