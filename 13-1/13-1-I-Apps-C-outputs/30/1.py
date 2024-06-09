
import math

def solve(N, k, heights):
    # Calculate the average height of the neighbors
    avg_height = sum(heights) / N
    
    # Calculate the new height for each house
    new_heights = []
    for i in range(N):
        if heights[i] >= avg_height + k:
            new_heights.append(heights[i])
        else:
            new_heights.append(avg_height + k)
    
    # Calculate the final height of the tallest house
    final_height = max(new_heights)
    
    return final_height

N, k = map(int, input().split())
heights = list(map(float, input().split()))
print(solve(N, k, heights))

