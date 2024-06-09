
def parse_expression(expression):
    # Convert the expression to a list of tokens
    tokens = expression.split()
    
    # Initialize the stack to hold the operators and operands
    stack = []
    
    # Iterate over the tokens
    for token in tokens:
        # If the token is a left parenthesis, push it to the stack
        if token == "(":
            stack.append(token)
        # If the token is a right parenthesis, pop the top element from the stack and check if it is a left parenthesis
        elif token == ")":
            top = stack.pop()
            if top != "(":
                return None
        # If the token is a number, push it to the stack
        elif token.isdigit():
            stack.append(int(token))
        # If the token is an operator, pop the top two elements from the stack, apply the operator, and push the result back to the stack
        elif token in ["+", "-"]:
            if len(stack) < 2:
                return None
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                result = left + right
            else:
                result = left - right
            stack.append(result)
    
    # If the stack contains a single element, return it as the result
    if len(stack) == 1:
        return stack.pop()
    else:
        return None

def find_max_value(expression, num_plus, num_minus):
    # Insert the plus and minus operators into the expression
    expression = expression.replace("?", "+")
    for _ in range(num_minus):
        expression = expression.replace("+", "-", 1)
    
    # Evaluate the expression and return the result
    return parse_expression(expression)

if __name__ == '__main__':
    expression = input()
    num_plus, num_minus = map(int, input().split())
    print(find_max_value(expression, num_plus, num_minus))

