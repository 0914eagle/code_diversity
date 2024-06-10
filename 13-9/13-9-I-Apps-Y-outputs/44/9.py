
import random

def evaluate_expression(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split('+')
    
    # Initialize a list to store the results
    results = []
    
    # Loop through each token and evaluate it
    for i in range(len(tokens)):
        # If the token is a plus symbol, randomly choose whether to interpret it as addition or string concatenation
        if tokens[i] == '+':
            if random.randint(0, 1) == 0:
                results.append(tokens[i-1] + tokens[i+1])
            else:
                results.append(tokens[i-1] + '+' + tokens[i+1])
        # If the token is an integer, append it to the results list
        else:
            results.append(tokens[i])
    
    # Return the number of distinct integers in the results list
    return len(set(results))

def main():
    expression = input("Enter an expression: ")
    print(evaluate_expression(expression))

if __name__ == '__main__':
    main()

