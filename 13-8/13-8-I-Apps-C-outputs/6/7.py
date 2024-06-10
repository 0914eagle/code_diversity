
def get_rebus_solution(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a set to store the numbers used in the rebus
    numbers = set()
    
    # Iterate over the tokens and check if they are integers or arithmetic operations
    for token in tokens:
        if token.isdigit():
            # If the token is an integer, add it to the set of numbers
            numbers.add(int(token))
        elif token in ['+', '-']:
            # If the token is an arithmetic operation, continue to the next token
            continue
        else:
            # If the token is not an integer or arithmetic operation, the rebus is invalid
            return "Impossible"
    
    # Check if the set of numbers is equal to the range of integers from 1 to n
    if len(numbers) == range(1, int(tokens[-1]) + 1):
        # If the set of numbers is equal to the range of integers, the rebus has a solution
        return "Possible"
    else:
        # If the set of numbers is not equal to the range of integers, the rebus does not have a solution
        return "Impossible"

def replace_question_marks(rebus, solution):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a dictionary to store the mapping from question marks to integers
    mapping = {}
    
    # Iterate over the tokens and check if they are integers or arithmetic operations
    for i, token in enumerate(tokens):
        if token.isdigit():
            # If the token is an integer, add it to the set of numbers
            mapping[i] = int(token)
        elif token in ['+', '-']:
            # If the token is an arithmetic operation, continue to the next token
            continue
        else:
            # If the token is not an integer or arithmetic operation, the rebus is invalid
            return "Impossible"
    
    # Replace the question marks with the corresponding integers from the solution
    for i, token in enumerate(tokens):
        if token == '?':
            tokens[i] = str(solution[i])
    
    # Return the rebus with question marks replaced by integers
    return " ".join(tokens)

if __name__ == '__main__':
    rebus = input()
    solution = get_rebus_solution(rebus)
    if solution == "Possible":
        print(replace_question_marks(rebus, solution))
    else:
        print(solution)

