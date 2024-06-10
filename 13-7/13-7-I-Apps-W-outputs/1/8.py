
def get_max_candies(n, x, h, m):
    # Initialize variables
    max_candies = 0
    current_height = x
    current_type = 0
    types = [0] * n
    heights = [0] * n
    masses = [0] * n
    
    # Loop through the input
    for i in range(n):
        types[i], heights[i], masses[i] = map(int, input().split())
    
    # Loop through the candies
    for i in range(n):
        # Check if the current candy is reachable
        if heights[i] <= current_height:
            # Check if the current candy has the same type as the previous candy
            if types[i] != current_type:
                # Eat the candy and update the variables
                current_height += masses[i]
                current_type = types[i]
                max_candies += 1
    
    # Return the maximum number of candies that can be eaten
    return max_candies

def main():
    # Read the input
    n, x = map(int, input().split())
    h = [0] * n
    m = [0] * n
    for i in range(n):
        h[i], m[i] = map(int, input().split())
    
    # Call the function to get the maximum number of candies
    max_candies = get_max_candies(n, x, h, m)
    
    # Print the result
    print(max_candies)

if __name__ == '__main__':
    main()

