
def get_rebus_solution(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    # Initialize a dictionary to store the solutions for each question mark
    solutions = {}
    # Iterate over the tokens and check if they are question marks or numbers
    for i, token in enumerate(tokens):
        if token == '?':
            # If the token is a question mark, assign it a value from 1 to n
            solutions[i] = i + 1
        else:
            # If the token is a number, check if it is equal to the sum of the previous numbers
            if i > 0 and tokens[i - 1] == '-':
                # If the previous token is a minus sign, subtract the current number from the previous solution
                solutions[i - 1] -= int(token)
            else:
                # If the previous token is not a minus sign, add the current number to the previous solution
                solutions[i - 1] += int(token)
    # Check if the last solution is equal to the target number
    if solutions[len(tokens) - 1] == int(tokens[-1]):
        # If it is, return the solutions as a string
        return 'Possible\n' + ' + '.join(str(solutions[i]) for i in solutions) + ' = ' + tokens[-1]
    else:
        # If it is not, return "Impossible"
        return 'Impossible'

def main():
    # Read a rebus from input
    rebus = input()
    # Call the get_rebus_solution function and print the result
    print(get_rebus_solution(rebus))

if __name__ == '__main__':
    main()

