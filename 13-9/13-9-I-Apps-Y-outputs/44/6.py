
import random

def evaluate_expression(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split('+')
    
    # Initialize a set to store the distinct integers
    distinct_integers = set()
    
    # Iterate through the list of tokens
    for i in range(len(tokens)):
        # If the token is an integer, add it to the set of distinct integers
        if tokens[i].isdigit():
            distinct_integers.add(int(tokens[i]))
        # If the token is a plus symbol, randomly decide whether to use addition or string concatenation
        elif tokens[i] == '+':
            if random.choice([True, False]):
                distinct_integers.add(str(distinct_integers.pop()) + str(distinct_integers.pop()))
            else:
                distinct_integers.add(distinct_integers.pop() + distinct_integers.pop())
    
    # Return the number of distinct integers
    return len(distinct_integers)

def main():
    expression = input("Enter an expression: ")
    print(evaluate_expression(expression))

if __name__ == '__main__':
    main()

