
def parse_expression(expression):
    
    # Convert the expression to a list of tokens
    tokens = expression.split()
    
    # Initialize the coefficient, variable, and constant to 0
    coefficient, variable, constant = 0, "", 0
    
    # Iterate over the tokens
    for token in tokens:
        # If the token is a number, add it to the constant
        if token.isdigit():
            constant += int(token)
        # If the token is a variable, set the variable name
        elif token.isalpha():
            variable = token
        # If the token is an operator, add it to the coefficient
        elif token in ["+", "-", "*"]:
            coefficient += 1
    
    return coefficient, variable, constant

def find_minimal_value(expression, p, m):
    
    # Parse the expression
    coefficient, variable, constant = parse_expression(expression)
    
    # Initialize the minimal value of x to 0
    minimal_value = 0
    
    # Iterate over all possible values of x
    for x in range(0, m):
        # Calculate the value of the expression with the current value of x
        value = coefficient * x ** 2 + constant
        
        # If the value is equal to p, return the current value of x
        if value % m == p:
            return x
        
        # If the value is greater than p, update the minimal value of x
        if value > p:
            minimal_value = x + 1
    
    # If no value of x was found, return the minimal value of x
    return minimal_value

def main():
    # Read the expression, p, and m from stdin
    expression, p, m = input().split()
    
    # Find the minimal non-negative value of variable x in the given expression so that the remainder of dividing the expression with m is equal to p
    result = find_minimal_value(expression, int(p), int(m))
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

