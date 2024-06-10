
def rebus_solver(rebus):
    # Split the rebus into a list of tokens
    tokens = rebus.split()
    # Initialize a list to store the values of the question marks
    values = []
    # Initialize a set to store the values of the arithmetic operations
    operations = set()
    # Iterate over the tokens
    for token in tokens:
        # If the token is a question mark, add it to the values list
        if token == "?":
            values.append(token)
        # If the token is an arithmetic operation, add it to the operations set
        elif token in "+-=":
            operations.add(token)
    # If there are an odd number of question marks, the rebus is impossible
    if len(values) % 2 == 1:
        return "Impossible"
    # If there are an odd number of arithmetic operations, the rebus is impossible
    if len(operations) % 2 == 1:
        return "Impossible"
    # If the number of question marks is not equal to the number of arithmetic operations, the rebus is impossible
    if len(values) != len(operations) + 1:
        return "Impossible"
    # If the number of question marks is not equal to the number of integers in the rebus, the rebus is impossible
    if len(values) != len(rebus.split("=")[0].split()) - 1:
        return "Impossible"
    # If the rebus is possible, return "Possible" followed by the rebus with the question marks replaced by integers from 1 to n
    return "Possible\n" + rebus.replace("?", "1")

def main():
    rebus = input()
    print(rebus_solver(rebus))

if __name__ == '__main__':
    main()

