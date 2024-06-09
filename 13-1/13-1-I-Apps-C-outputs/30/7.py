
import math

def get_final_height(N, k, heights):
    # Initialize the final heights array
    final_heights = [0] * N
    # Set the final height of the first and last houses to be the initial height
    final_heights[0] = heights[0]
    final_heights[N-1] = heights[N-1]
    
    # Iterate through the houses
    for i in range(1, N-1):
        # Calculate the average height of the neighbors
        avg_height = (heights[i-1] + heights[i+1]) / 2
        # Calculate the new height
        new_height = avg_height + k
        # Update the final height
        final_heights[i] = new_height
    
    # Return the final height of the tallest house
    return max(final_heights)

# Test the function with the sample input
N = 3
k = 1
heights = [39, 10, 40]
print(get_final_height(N, k, heights))

