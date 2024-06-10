
import random

def generate_expression(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split()
    
    # Initialize a list to store the evaluated expressions
    evaluated_expressions = []
    
    # Iterate through the tokens and evaluate the expression
    for i in range(len(tokens)):
        # Check if the current token is a plus symbol
        if tokens[i] == "+":
            # Generate a random integer between 0 and 1
            random_int = random.randint(0, 1)
            
            # Check if the random integer is 0
            if random_int == 0:
                # Evaluate the expression as string concatenation
                evaluated_expression = str(tokens[i-1]) + str(tokens[i+1])
            else:
                # Evaluate the expression as addition
                evaluated_expression = int(tokens[i-1]) + int(tokens[i+1])
        else:
            # Evaluate the expression as an integer
            evaluated_expression = int(tokens[i])
        
        # Add the evaluated expression to the list of evaluated expressions
        evaluated_expressions.append(evaluated_expression)
    
    # Return the list of evaluated expressions
    return evaluated_expressions

def count_distinct_integers(evaluated_expressions):
    # Initialize a set to store the distinct integers
    distinct_integers = set()
    
    # Iterate through the evaluated expressions
    for evaluated_expression in evaluated_expressions:
        # Add the evaluated expression to the set of distinct integers
        distinct_integers.add(evaluated_expression)
    
    # Return the number of distinct integers
    return len(distinct_integers)

def main():
    # Read a line of input from stdin and split it into a list of integers and plus symbols
    expression = input().split()
    
    # Generate the evaluated expressions
    evaluated_expressions = generate_expression(expression)
    
    # Count the number of distinct integers
    count = count_distinct_integers(evaluated_expressions)
    
    # Print the number of distinct integers
    print(count)

if __name__ == '__main__':
    main()

