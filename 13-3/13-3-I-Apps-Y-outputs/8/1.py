
import random

def evaluate_expression(expression):
    tokens = expression.split("+")
    integers = [int(token) for token in tokens if token.isdigit()]
    plus_symbols = ["+" for token in tokens if token != ""]
    total_combinations = 2 ** (len(plus_symbols) - 1)
    distinct_integers = set()
    for i in range(total_combinations):
        combination = bin(i)[2:].zfill(len(plus_symbols))
        evaluated_expression = ""
        for j, token in enumerate(tokens):
            if token.isdigit():
                evaluated_expression += token
            else:
                if combination[j] == "0":
                    evaluated_expression += "+"
                else:
                    evaluated_expression += " "
        evaluated_expression = evaluated_expression.strip()
        if evaluated_expression.isdigit():
            distinct_integers.add(int(evaluated_expression))
    return len(distinct_integers)

if __name__ == "__main__":
    expression = input()
    print(evaluate_expression(expression))

