
def get_possible_suspects(n, p):
    # Initialize a set to store the possible suspects
    possible_suspects = set()
    
    # Iterate over each coder
    for i in range(1, n + 1):
        # Get the names of the two coders named by the current coder
        x, y = map(int, input().split())
        
        # If at least one of the two coders is not the current coder, add them to the possible suspects set
        if x != i and y != i:
            possible_suspects.add(x)
            possible_suspects.add(y)
    
    # Return the number of possible suspects that at least p coders agreed with
    return len(possible_suspects)

def main():
    # Read the input
    n, p = map(int, input().split())
    
    # Call the get_possible_suspects function and print the result
    print(get_possible_suspects(n, p))

if __name__ == '__main__':
    main()

