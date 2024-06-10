
def get_max_candies(n, x, heights, masses):
    # Initialize variables
    max_candies = 0
    current_height = x
    types = [0] * n
    i = 0
    
    # Iterate through the candies
    while i < n:
        # Check if the current candy is within reach
        if heights[i] <= current_height:
            # Eat the candy and update the variables
            max_candies += 1
            current_height += masses[i]
            types[i] = 1 - types[i]
            i += 1
        else:
            # If the candy is not within reach, move on to the next candy
            i += 1
    
    # Return the maximum number of candies that can be eaten
    return max_candies

def main():
    # Read the input
    n, x = map(int, input().split())
    heights = list(map(int, input().split()))
    masses = list(map(int, input().split()))
    
    # Call the function to get the maximum number of candies
    max_candies = get_max_candies(n, x, heights, masses)
    
    # Print the output
    print(max_candies)

if __name__ == '__main__':
    main()

