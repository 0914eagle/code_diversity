
def get_rebus_solution(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a dictionary to store the values of the variables
    variables = {}
    
    # Loop through each token and check if it is a variable or an operation
    for i, token in enumerate(tokens):
        if token.isalpha():
            # If the token is a variable, set its value to 0
            variables[token] = 0
        elif token in ["+", "-"]:
            # If the token is an operation, check if the previous token is a variable
            if tokens[i-1].isalpha():
                # If the previous token is a variable, set its value to the current token
                variables[tokens[i-1]] = int(tokens[i+1])
            else:
                # If the previous token is not a variable, return "Impossible"
                return "Impossible"
    
    # Check if the final token is equal to the target value
    if tokens[-2] == "=" and int(tokens[-1]) == sum(variables.values()):
        # If it is, return "Possible" and the rebus with the variables replaced by their values
        return "Possible", " = ".join([str(variables[token]) for token in tokens if token.isalpha()])
    
    # If the final token is not equal to the target value, return "Impossible"
    return "Impossible"

def main():
    # Read a line of input from stdin and split it into a list of tokens
    line = input().split()
    
    # Call the get_rebus_solution function and unpack the return value
    status, rebus = get_rebus_solution(" ".join(line))
    
    # Print the status and rebus (if applicable)
    print(status)
    if status == "Possible":
        print(rebus)

if __name__ == '__main__':
    main()

