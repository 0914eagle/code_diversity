
import re

def get_expression(expression):
    # Replace all ? with + or -
    expression = re.sub(r"\?", "?", expression)
    return expression

def evaluate_expression(expression):
    # Evaluate the expression using eval() function
    return eval(expression)

def solve(expression, num_plus, num_minus):
    # Get the original expression with ? instead of operators
    expression = get_expression(expression)
    
    # Replace ? with + or - based on the number of plus and minus operators
    for i in range(num_plus):
        expression = expression.replace("?", "+", 1)
    for i in range(num_minus):
        expression = expression.replace("?", "-", 1)
    
    # Evaluate the expression and return the result
    return evaluate_expression(expression)

if __name__ == '__main__':
    expression = input()
    num_plus, num_minus = map(int, input().split())
    print(solve(expression, num_plus, num_minus))

