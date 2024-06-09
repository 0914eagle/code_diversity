
def parse_expression(expression):
    # Convert the expression to a list of tokens
    tokens = expression.split()
    
    # Initialize the stack to hold the operators and operands
    stack = []
    
    # Iterate through the tokens
    for token in tokens:
        # If the token is a number, push it to the stack
        if token.isdigit():
            stack.append(int(token))
        # If the token is an operator, pop the top two elements from the stack, apply the operator, and push the result back to the stack
        elif token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(-stack.pop() + stack.pop())
    
    # The final result is at the top of the stack
    return stack.pop()

def get_max_value(expression, num_plus, num_minus):
    # Replace the ? characters with the appropriate operators
    expression = expression.replace('?', '+') * num_plus
    expression = expression.replace('?', '-') * num_minus
    
    # Parse the expression and return the maximum value
    return parse_expression(expression)

def main():
    expression, num_plus, num_minus = input().split()
    print(get_max_value(expression, int(num_plus), int(num_minus)))

if __name__ == '__main__':
    main()

