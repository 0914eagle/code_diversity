
def solve(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a set to store the values of the question marks
    values = set()
    
    # Iterate over the tokens and check if they are question marks or integers
    for token in tokens:
        if token == "?":
            # If the token is a question mark, add it to the set of values
            values.add(token)
        else:
            # If the token is an integer, check if it is positive and not greater than n
            value = int(token)
            if value <= 0 or value > n:
                return "Impossible"
    
    # If all tokens are valid, try to solve the rebus
    for value in values:
        # Replace the question mark with the current value and evaluate the expression
        expression = rebus.replace("?", str(value))
        result = eval(expression)
        
        # If the result is equal to n, return the rebus with the question marks replaced by the current value
        if result == n:
            return "Possible\n" + expression
    
    # If no value works, return "Impossible"
    return "Impossible"

def main():
    # Read a line of input from stdin and convert it to an integer
    n = int(input())
    
    # Read a line of input from stdin and convert it to a string
    rebus = input()
    
    # Call the solve function and print the result
    print(solve(rebus))

if __name__ == '__main__':
    main()

