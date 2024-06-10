
def get_expression_value(expression, x):
    # Replace all instances of x with x**2
    expression = expression.replace("x", "x**2")
    
    # Evaluate the expression
    return eval(expression)

def get_min_x(expression, p, m):
    # Initialize min_x to 0
    min_x = 0
    
    # Loop until we find a value of x that gives us the correct remainder
    while True:
        # Calculate the value of the expression with the current value of x
        value = get_expression_value(expression, min_x)
        
        # If the value is divisible by m with a remainder of p, we have found the minimum value of x
        if value % m == p:
            break
        
        # Otherwise, increment x by 1 and try again
        min_x += 1
    
    return min_x

def main():
    # Read the input expression and p, m from stdin
    expression, p, m = input().split()
    
    # Calculate the minimum value of x
    min_x = get_min_x(expression, int(p), int(m))
    
    # Print the result
    print(min_x)

if __name__ == '__main__':
    main()

