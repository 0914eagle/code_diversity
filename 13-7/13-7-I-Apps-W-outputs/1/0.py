
def get_max_candies(n, x, heights, masses):
    # Initialize variables
    max_candies = 0
    current_height = x
    current_mass = 0
    types = [0] * n
    i = 0
    
    # Loop through the candies
    while i < n:
        # Check if the current candy is within reach
        if heights[i] <= current_height:
            # Eat the candy and update the variables
            max_candies += 1
            current_height += masses[i]
            current_mass += masses[i]
            types[i] = 1 - types[i]
        i += 1
    
    # Return the maximum number of candies that can be eaten
    return max_candies

def main():
    n, x = map(int, input().split())
    heights = list(map(int, input().split()))
    masses = list(map(int, input().split()))
    print(get_max_candies(n, x, heights, masses))

if __name__ == '__main__':
    main()

