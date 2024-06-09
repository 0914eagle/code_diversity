
def get_final_height(heights, k):
    # Initialize the final heights array
    final_heights = [0] * len(heights)
    
    # Loop through each house and calculate the final height
    for i in range(len(heights)):
        # Calculate the average height of the neighboring houses
        avg_height = (heights[i-1] + heights[i+1]) / 2
        
        # Calculate the final height
        final_height = max(avg_height + k, heights[i])
        
        # Update the final heights array
        final_heights[i] = final_height
    
    # Return the final height of the tallest house
    return max(final_heights)

def main():
    # Read the input
    N, k = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # Calculate the final heights
    final_height = get_final_height(heights, k)
    
    # Print the final height
    print(final_height)

if __name__ == '__main__':
    main()

