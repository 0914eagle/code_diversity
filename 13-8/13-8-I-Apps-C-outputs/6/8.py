
def get_rebus_solution(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    # Initialize a list to store the possible solutions
    solutions = []
    # Iterate over the tokens and check if they are integers or arithmetic operations
    for token in tokens:
        if token.isdigit():
            # If the token is an integer, add it to the list of solutions
            solutions.append(int(token))
        elif token == '+':
            # If the token is a plus sign, combine the last two solutions
            # and add the result to the list of solutions
            solutions.append(solutions[-1] + solutions[-2])
        elif token == '-':
            # If the token is a minus sign, combine the last two solutions
            # and add the result to the list of solutions
            solutions.append(solutions[-1] - solutions[-2])
        elif token == '=':
            # If the token is an equals sign, check if the last solution is equal to the expected value
            if solutions[-1] == int(tokens[-1]):
                # If the last solution is equal to the expected value, return the list of solutions
                return solutions
            else:
                # If the last solution is not equal to the expected value, return None
                return None
    # If the rebus is not valid, return None
    return None

def get_rebus_solution_input():
    # Get the rebus from the input
    rebus = input("Enter the rebus: ")
    # Call the get_rebus_solution function and get the list of solutions
    solutions = get_rebus_solution(rebus)
    # If the list of solutions is not None, print the possible solution
    if solutions is not None:
        print("Possible")
        # Print the solution with the question marks replaced by the integers from 1 to n
        print(" + ".join(str(solution) for solution in solutions))
    else:
        print("Impossible")

if __name__ == '__main__':
    get_rebus_solution_input()

