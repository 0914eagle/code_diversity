
def get_expression_value(expression, x):
    # Replace all instances of x with x**2 in the expression
    expression = expression.replace("x", "x**2")
    
    # Evaluate the expression using eval() function
    return eval(expression)

def get_min_x(expression, p, m):
    # Initialize min_x to 0
    min_x = 0
    
    # Iterate from 0 to m-1
    for i in range(m):
        # Calculate the value of the expression with x set to i
        value = get_expression_value(expression, i)
        
        # If the value is equal to p, set min_x to i and break
        if value == p:
            min_x = i
            break
    
    # Return the minimum value of x
    return min_x

def main():
    # Read the expression, p, and m from input
    expression, p, m = input().split()
    
    # Calculate the minimum value of x
    min_x = get_min_x(expression, int(p), int(m))
    
    # Print the minimum value of x
    print(min_x)

if __name__ == '__main__':
    main()

