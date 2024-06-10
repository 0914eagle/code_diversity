
import random

def evaluate_expression(expression):
    tokens = expression.split("+")
    result = int(tokens[0])
    for i in range(1, len(tokens) - 1):
        if random.randint(0, 1) == 0:
            result += int(tokens[i])
        else:
            result = str(result) + tokens[i]
    return result

def count_distinct_integers(expression):
    results = set()
    for i in range(100):
        results.add(evaluate_expression(expression))
    return len(results)

if __name__ == '__main__':
    expression = input()
    print(count_distinct_integers(expression))

