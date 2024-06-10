
def is_rebus_solvable(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a dictionary to store the values of the question marks
    values = {}
    
    # Iterate over the tokens and check if they are question marks or integers
    for token in tokens:
        if token.isdigit():
            # If the token is an integer, add it to the dictionary with a value of 0
            values[token] = 0
        elif token == '?':
            # If the token is a question mark, add it to the dictionary with a value of -1
            values[token] = -1
    
    # Iterate over the tokens again and check if they are arithmetic operations
    for token in tokens:
        if token in ['+', '-']:
            # If the token is an arithmetic operation, get the values of the two numbers on either side of it
            num1 = int(tokens[tokens.index(token) - 1])
            num2 = int(tokens[tokens.index(token) + 1])
            
            # Check if the values of the two numbers are in the dictionary
            if num1 in values and num2 in values:
                # If they are, add the result of the arithmetic operation to the dictionary with the question mark as the key
                values['?'] = values[num1] + values[num2] if token == '+' else values[num1] - values[num2]
            else:
                # If they are not, return False
                return False
    
    # If we have reached the end of the loop, check if the value of the final question mark is equal to the target value
    if values['?'] == int(tokens[-1]):
        # If it is, return True
        return True
    else:
        # If it is not, return False
        return False

def solve_rebus(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a dictionary to store the values of the question marks
    values = {}
    
    # Iterate over the tokens and check if they are question marks or integers
    for token in tokens:
        if token.isdigit():
            # If the token is an integer, add it to the dictionary with a value of 0
            values[token] = 0
        elif token == '?':
            # If the token is a question mark, add it to the dictionary with a value of -1
            values[token] = -1
    
    # Iterate over the tokens again and check if they are arithmetic operations
    for token in tokens:
        if token in ['+', '-']:
            # If the token is an arithmetic operation, get the values of the two numbers on either side of it
            num1 = int(tokens[tokens.index(token) - 1])
            num2 = int(tokens[tokens.index(token) + 1])
            
            # Check if the values of the two numbers are in the dictionary
            if num1 in values and num2 in values:
                # If they are, add the result of the arithmetic operation to the dictionary with the question mark as the key
                values['?'] = values[num1] + values[num2] if token == '+' else values[num1] - values[num2]
            else:
                # If they are not, return False
                return False
    
    # If we have reached the end of the loop, check if the value of the final question mark is equal to the target value
    if values['?'] == int(tokens[-1]):
        # If it is, return True
        return True
    else:
        # If it is not, return False
        return False

def main():
    rebus = input("Enter a rebus: ")
    if solve_rebus(rebus):
        print("Possible")
        print(rebus)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()

