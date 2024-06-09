
def get_possible_two_suspect_sets(n, p, coders):
    # Initialize a set to store the possible two-suspect sets
    possible_sets = set()
    
    # Iterate over each coder
    for coder in coders:
        # Get the names of the two coders mentioned by the current coder
        x, y = coder
        
        # If the current coder agrees with the head's choice, add the two-suspect set to the possible sets
        if x in possible_sets or y in possible_sets:
            possible_sets.add((x, y))
    
    # Return the number of possible two-suspect sets
    return len(possible_sets)

def main():
    # Read the input n, p, and coders
    n, p = map(int, input().split())
    coders = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Call the function to get the number of possible two-suspect sets
    possible_sets = get_possible_two_suspect_sets(n, p, coders)
    
    # Print the number of possible two-suspect sets
    print(possible_sets)

if __name__ == '__main__':
    main()

