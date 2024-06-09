
def get_final_height(houses, k):
    # Initialize the final height of each house
    final_heights = [0] * len(houses)
    
    # Loop through each house and calculate the final height
    for i in range(len(houses)):
        # Calculate the average height of the neighboring houses
        avg_height = (final_heights[i-1] + final_heights[i+1]) / 2 if i > 0 and i < len(houses) - 1 else 0
        
        # Check if the current house is taller than the average plus k
        if houses[i] >= avg_height + k:
            # If it is, set the final height to the current height
            final_heights[i] = houses[i]
        else:
            # If it's not, set the final height to the average plus k
            final_heights[i] = avg_height + k
    
    # Return the height of the tallest house
    return max(final_heights)

def main():
    # Read the input
    N, k = map(int, input().split())
    houses = list(map(int, input().split()))
    
    # Calculate the final heights of the houses
    final_height = get_final_height(houses, k)
    
    # Print the final height
    print(final_height)

if __name__ == '__main__':
    main()

