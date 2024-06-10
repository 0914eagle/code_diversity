
def get_two_suspects(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    
    # Iterate over the coders and their names
    for coder, names in coders.items():
        # If the coder has agreed with the choice of two suspects
        if len(suspects.intersection(names)) >= 1:
            # Add the coder to the set of suspects
            suspects.add(coder)
    
    # Return the number of possible two-suspect sets
    return len(list(combinations(suspects, 2)))

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = {}
    for i in range(n):
        x, y = map(int, input().split())
        coders[i+1] = {x, y}
    
    # Print the number of possible two-suspect sets
    print(get_two_suspects(n, p, coders))

if __name__ == '__main__':
    main()

