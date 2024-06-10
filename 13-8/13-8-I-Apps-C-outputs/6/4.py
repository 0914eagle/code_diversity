
def rebus_solver(rebus):
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
            # If the token is an integer, check if it is within the range of the rebus
            value = int(token)
            if value < 1 or value > 1000000:
                return "Impossible"
    
    # If the set of values is empty, return "Impossible"
    if not values:
        return "Impossible"
    
    # If the set of values has only one element, return "Possible" with the rebus solved
    if len(values) == 1:
        return "Possible\n" + rebus.replace("?", str(values.pop()))
    
    # If the set of values has more than one element, return "Impossible"
    return "Impossible"

def main():
    rebus = input()
    print(rebus_solver(rebus))

if __name__ == '__main__':
    main()

