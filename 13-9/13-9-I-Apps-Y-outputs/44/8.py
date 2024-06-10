
import random

def evaluate_expression(expression):
    tokens = expression.split('+')
    integers = [int(token) for token in tokens if token.isdigit()]
    plus_symbols = ['+' for token in tokens if token != '']
    
    combinations = []
    for i in range(len(integers)):
        combinations.append([integers[i]])
        for j in range(i+1, len(integers)):
            combinations.append([integers[i], integers[j]])
    
    results = set()
    for combination in combinations:
        result = sum(combination)
        results.add(result)
    
    return len(results)

def main():
    expression = input()
    print(evaluate_expression(expression))

if __name__ == '__main__':
    main()

