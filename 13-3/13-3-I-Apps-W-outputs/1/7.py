
def count_attacking_pairs(bishops):
    # Initialize a set to store the positions of the bishops
    positions = set()
    # Initialize a counter for the number of attacking pairs
    attacking_pairs = 0
    
    # Iterate over the bishops
    for bishop in bishops:
        # Get the position of the current bishop
        x, y = bishop
        # Check if the position is already in the set of positions
        if (x, y) in positions:
            # If the position is already in the set, it means that there is another bishop on the same diagonal, so we need to count this as an attacking pair
            attacking_pairs += 1
        else:
            # If the position is not in the set, we add it to the set and continue
            positions.add((x, y))
    
    # Return the number of attacking pairs
    return attacking_pairs

def main():
    # Read the number of bishops from stdin
    n = int(input())
    # Read the positions of the bishops from stdin
    bishops = []
    for _ in range(n):
        x, y = map(int, input().split())
        bishops.append((x, y))
    # Call the count_attacking_pairs function and print the result
    print(count_attacking_pairs(bishops))

if __name__ == '__main__':
    main()

