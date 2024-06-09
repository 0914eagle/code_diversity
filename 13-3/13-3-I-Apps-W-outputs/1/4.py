
def count_attacking_pairs(n, bishops):
    # Initialize a set to store the positions of the bishops
    positions = set()
    # Initialize a counter for the number of attacking pairs
    attacking_pairs = 0
    
    # Loop through each bishop
    for i in range(n):
        # Get the position of the current bishop
        x, y = bishops[i]
        # Check if the position is already in the set of positions
        if (x, y) in positions:
            # If it is, it means that there is another bishop on the same diagonal, so we increment the counter
            attacking_pairs += 1
        else:
            # If it's not, we add it to the set of positions
            positions.add((x, y))
    
    # Return the number of attacking pairs
    return attacking_pairs

def main():
    # Read the number of bishops from stdin
    n = int(input())
    # Read the positions of the bishops from stdin
    bishops = []
    for i in range(n):
        x, y = map(int, input().split())
        bishops.append((x, y))
    # Call the count_attacking_pairs function and print the result
    print(count_attacking_pairs(n, bishops))

if __name__ == '__main__':
    main()

