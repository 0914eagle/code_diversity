
def rebus_solver(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    
    # Initialize a list to store the answers
    answers = []
    
    # Iterate over the tokens
    for token in tokens:
        # If the token is a question mark, add it to the answers list
        if token == "?":
            answers.append(token)
        # If the token is an integer, convert it to an int and add it to the answers list
        elif token.isdigit():
            answers.append(int(token))
        # If the token is an arithmetic operation, perform the operation on the last two elements of the answers list
        elif token in ["+", "-"]:
            # Get the last two elements of the answers list
            last_two = answers[-2:]
            # Perform the operation
            if token == "+":
                result = last_two[0] + last_two[1]
            else:
                result = last_two[0] - last_two[1]
            # Add the result to the answers list
            answers.append(result)
        # If the token is an equality sign, check if the last element of the answers list is equal to the integer following the equality sign
        elif token == "=":
            # Get the last element of the answers list
            last_element = answers[-1]
            # Get the integer following the equality sign
            target = int(tokens[tokens.index(token) + 1])
            # Check if the last element is equal to the target
            if last_element == target:
                return "Possible", " ".join(map(str, answers))
            else:
                return "Impossible", None
    
    # If the rebus is not solvable, return "Impossible"
    return "Impossible", None

def main():
    rebus = input("Enter a rebus: ")
    result = rebus_solver(rebus)
    print(result[0])
    if result[0] == "Possible":
        print(result[1])

if __name__ == '__main__':
    main()

