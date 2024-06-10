
def get_suspects(n, p, coders):
    # Initialize a set to store the suspects
    suspects = set()
    
    # Iterate over the coders
    for coder in coders:
        # If the coder agreed with the head's choice, add their suspects to the set
        if coder[0] in suspects or coder[1] in suspects:
            suspects.add(coder[0])
            suspects.add(coder[1])
    
    # Return the number of unique suspects
    return len(suspects)

def count_possible_two_suspect_sets(n, p, coders):
    # Initialize a variable to store the number of possible two-suspect sets
    possible_sets = 0
    
    # Iterate over the coders
    for i in range(n):
        # Get the suspects for the current coder
        suspects = get_suspects(n, p, coders[i:])
        
        # If the current coder has at least p agreed coders, add their suspects to the set
        if suspects >= p:
            possible_sets += 1
    
    # Return the number of possible two-suspect sets
    return possible_sets

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coders.append(tuple(map(int, input().split())))
    
    # Call the function to count the possible two-suspect sets
    possible_sets = count_possible_two_suspect_sets(n, p, coders)
    
    # Print the result
    print(possible_sets)

if __name__ == '__main__':
    main()

