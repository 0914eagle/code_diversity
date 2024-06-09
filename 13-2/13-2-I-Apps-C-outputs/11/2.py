
def solve(N, k, heights):
    # Calculate the average height of the neighbors
    avg_height = sum(heights) / N
    
    # Calculate the final height of each house
    final_heights = []
    for i in range(N):
        if heights[i] >= avg_height + k:
            final_heights.append(heights[i])
        else:
            final_heights.append((heights[i-1] + heights[i+1]) / 2 + k)
    
    # Return the height of the tallest house
    return max(final_heights)

