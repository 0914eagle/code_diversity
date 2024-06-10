
import random

def parse_expression(expression):
    # Split the expression into a list of integers and plus symbols
    tokens = expression.split('+')
    
    # Initialize a set to store the distinct integers
    distinct_integers = set()
    
    # Iterate through the list of tokens
    for i in range(len(tokens)):
        # If the current token is an integer, add it to the set of distinct integers
        if tokens[i].isdigit():
            distinct_integers.add(int(tokens[i]))
        # If the current token is a plus symbol, choose a random integer to concatenate with the previous integer
        elif tokens[i] == '+':
            # Choose a random integer to concatenate with the previous integer
            random_integer = random.randint(0, 9)
            # Concatenate the previous integer with the random integer
            concatenated_integer = str(int(tokens[i-1]) * 10 + random_integer)
            # Add the concatenated integer to the set of distinct integers
            distinct_integers.add(int(concatenated_integer))
    
    # Return the number of distinct integers
    return len(distinct_integers)

def main():
    # Read a line of input from stdin and convert it to an integer list
    expression = input().split('+')
    
    # Call the parse_expression function and print the result
    print(parse_expression(expression))

if __name__ == '__main__':
    main()

