
def get_arrangements(n_colors, colors, forbidden, sequence):
    # Initialize a list to store the arrangements
    arrangements = []
    
    # Iterate through each possible arrangement
    for i in range(n_colors):
        # Check if the current color is not in the forbidden list
        if colors[i] not in forbidden:
            # Check if the current color is in the sequence
            if i in sequence:
                # If it is, add it to the arrangements list
                arrangements.append(i)
    
    # Return the number of arrangements
    return len(arrangements)

def main():
    # Read the input
    n_colors, n_balls = map(int, input().split())
    colors = list(map(int, input().split()))
    forbidden = list(map(int, input().split()))
    sequence = list(map(int, input().split()))
    
    # Call the get_arrangements function
    arrangements = get_arrangements(n_colors, colors, forbidden, sequence)
    
    # Print the result
    print(arrangements)

if __name__ == '__main__':
    main()

