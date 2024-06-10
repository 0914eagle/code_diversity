
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
        
        # Check if the current candy is within reach
        if current_height >= heights[i]:
            # Eat the candy and update the height
            current_height += masses[i]
            max_candies += 1
            
            # Update the current type
            current_type = types[i]
            
    return max_candies

def main():
    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    m = list(map(int, input().split()))
    result = get_max_candies(n, x, h, m)
    print(result)

if __name__ == '__main__':
    main()

