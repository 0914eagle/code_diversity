
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
        types[i] = h[i]
        heights[i] = h[i]
        masses[i] = m[i]
        
        # Check if the current candy is reachable
        if heights[i] <= current_height:
            # Eat the candy and update the variables
            max_candies += 1
            current_height += masses[i]
            current_type = types[i]
        else:
            # Check if the current candy is of a different type than the previous candy
            if current_type != types[i]:
                # Eat the candy and update the variables
                max_candies += 1
                current_height += masses[i]
                current_type = types[i]
    
    # Return the maximum number of candies that can be eaten
    return max_candies

def main():
    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    m = list(map(int, input().split()))
    print(get_max_candies(n, x, h, m))

if __name__ == '__main__':
    main()

