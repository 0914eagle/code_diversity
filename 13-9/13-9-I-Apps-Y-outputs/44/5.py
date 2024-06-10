
import random

def evaluate_expression(expression):
    tokens = expression.split("+")
    result = int(tokens[0])
    for i in range(1, len(tokens) - 1):
        if random.randint(0, 1) == 0:
            result += int(tokens[i])
        else:
            result = str(result) + tokens[i]
    if random.randint(0, 1) == 0:
        result += int(tokens[-1])
    else:
        result = str(result) + tokens[-1]
    return result

def main():
    expression = input("Enter an expression: ")
    print(evaluate_expression(expression))

if __name__ == '__main__':
    main()

