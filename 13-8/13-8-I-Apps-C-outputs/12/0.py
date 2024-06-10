
def get_two_suspects(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    
    # Iterate over the coders
    for coder in coders:
        # If the coder agreed with the choice of two suspects
        if coder[0] in suspects or coder[1] in suspects:
            # Add the other coder to the set of suspects
            suspects.add(coder[0] if coder[1] in suspects else coder[1])
    
    # Return the number of suspects
    return len(suspects)

def count_possible_two_suspect_sets(n, p, coders):
    # Initialize a variable to store the number of possible two-suspect sets
    possible_sets = 0
    
    # Iterate over the coders
    for i in range(n):
        # Get the two suspects for the current coder
        suspects = get_two_suspects(n, p, coders[i:])
        
        # If the current coder agreed with the choice of two suspects
        if suspects >= p:
            # Increment the number of possible two-suspect sets
            possible_sets += 1
    
    # Return the number of possible two-suspect sets
    return possible_sets

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Print the number of possible two-suspect sets
    print(count_possible_two_suspect_sets(n, p, coders))

if __name__ == '__main__':
    main()

