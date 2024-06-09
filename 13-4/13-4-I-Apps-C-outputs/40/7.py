
def get_final_height(heights, k):
    # Initialize the final heights array
    final_heights = [0] * len(heights)
    
    # Loop through each house and calculate the final height
    for i in range(len(heights)):
        # Calculate the average height of the neighboring houses
        avg_height = (heights[i-1] + heights[i+1]) / 2
        
        # Check if the current house is taller than the average plus k
        if heights[i] >= avg_height + k:
            # If it is, set the final height to the current height
            final_heights[i] = heights[i]
        else:
            # If it's not, set the final height to the average plus k
            final_heights[i] = avg_height + k
    
    # Return the final heights array
    return final_heights

def main():
    # Read the input
    N, k = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # Calculate the final heights
    final_heights = get_final_height(heights, k)
    
    # Print the final height of the tallest house
    print(max(final_heights))

if __name__ == '__main__':
    main()

