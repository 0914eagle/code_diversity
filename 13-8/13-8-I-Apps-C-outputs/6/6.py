
def is_valid_rebus(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a stack to hold the operators
    op_stack = []
    
    # Initialize a stack to hold the numbers
    num_stack = []
    
    # Iterate through the tokens
    for token in tokens:
        # If the token is a number, push it onto the number stack
        if token.isdigit():
            num_stack.append(int(token))
        # If the token is an operator, push it onto the operator stack
        elif token in ['+', '-']:
            op_stack.append(token)
        # If the token is '=', pop the top two numbers from the number stack, perform the appropriate operation, and push the result back onto the number stack
        elif token == '=':
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            if op_stack.pop() == '+':
                num_stack.append(num1 + num2)
            else:
                num_stack.append(num1 - num2)
    
    # If the number stack contains a single element and it is equal to the target number, return True
    if len(num_stack) == 1 and num_stack[0] == int(tokens[-1]):
        return True
    # Otherwise, return False
    else:
        return False

def solve_rebus(rebus):
    # Initialize a list to hold the possible solutions
    solutions = []
    
    # Iterate through the possible values of the first question mark
    for i in range(1, int(tokens[-1]) + 1):
        # If the rebus is valid with the current value of the first question mark, add it to the list of solutions
        if is_valid_rebus(rebus.replace('?', str(i))):
            solutions.append(rebus.replace('?', str(i)))
    
    # If there are no solutions, return "Impossible"
    if not solutions:
        return "Impossible"
    # Otherwise, return any one of the solutions
    else:
        return solutions[0]

if __name__ == '__main__':
    rebus = input()
    print(solve_rebus(rebus))

