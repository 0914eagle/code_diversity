
def get_possible_suspects(n, p, coders):
    # Initialize a set to store the possible suspects
    possible_suspects = set()
    
    # Iterate over each coder
    for i in range(n):
        # Get the names of the two coders who claimed responsibility
        x, y = coders[i]
        
        # If both coders are in the list of possible suspects, add them to the set of possible suspects
        if x in possible_suspects and y in possible_suspects:
            possible_suspects.add(i + 1)
    
    # Return the number of possible suspects that have at least p agreements with the head of the company
    return len([suspect for suspect in possible_suspects if len([coder for coder in coders if suspect in coder]) >= p])

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coders.append(tuple(map(int, input().split())))
    
    # Call the function to get the number of possible suspects
    possible_suspects = get_possible_suspects(n, p, coders)
    
    # Print the result
    print(possible_suspects)

if __name__ == '__main__':
    main()

