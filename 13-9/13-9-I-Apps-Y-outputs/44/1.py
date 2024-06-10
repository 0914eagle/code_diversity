
import random

def get_input():
    return input().split('+')

def evaluate_expression(expression):
    result = 0
    for i in range(0, len(expression), 2):
        result += int(expression[i])
    for i in range(1, len(expression), 2):
        result += int(expression[i])
    return result

def get_distinct_integers(expression):
    result = set()
    for _ in range(1000):
        random.shuffle(expression)
        result.add(evaluate_expression(expression))
    return len(result)

def main():
    expression = get_input()
    print(get_distinct_integers(expression))

if __name__ == '__main__':
    main()

