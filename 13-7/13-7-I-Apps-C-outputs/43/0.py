
import re

def is_valid_expression(expression):
    
    pattern = r"^[0-9()+*-]+$"
    if not re.match(pattern, expression):
        return False
    if expression.count("(") != expression.count(")"):
        return False
    if expression.count("*") > 1:
        return False
    return True

def get_min_x(expression, p, m):
    
    # Check if the expression is valid
    if not is_valid_expression(expression):
        raise ValueError("Invalid expression")
    
    # Convert the expression to a polynomial of the first degree in x
    polynomial = convert_to_polynomial(expression)
    
    # Find the roots of the polynomial
    roots = find_roots(polynomial, m)
    
    # Return the minimum non-negative root
    return min(root for root in roots if root >= 0)

def convert_to_polynomial(expression):
    
    # Replace all instances of x with 1
    expression = expression.replace("x", "1")
    
    # Evaluate the expression and convert it to a polynomial
    polynomial = str(eval(expression))
    
    return polynomial

def find_roots(polynomial, m):
    
    # Find the remainder of dividing the polynomial by m
    remainder = polynomial % m
    
    # Find the roots of the remainder
    roots = [remainder // m]
    
    return roots

if __name__ == '__main__':
    expression, p, m = input().split()
    print(get_min_x(expression, int(p), int(m)))

