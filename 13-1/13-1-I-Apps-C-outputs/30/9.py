
import math

def solve(N, k, heights):
    # Calculate the average height of the houses
    avg_height = sum(heights) / N
    
    # Calculate the new height for each house
    new_heights = []
    for i in range(N):
        if heights[i] >= avg_height + k:
            new_heights.append(heights[i])
        else:
            new_heights.append((heights[i-1] + heights[i+1]) / 2 + k)
    
    # Check if all houses have converged to a final height
    if new_heights == heights:
        return max(new_heights)
    else:
        return solve(N, k, new_heights)

def main():
    N, k = map(int, input().split())
    heights = list(map(float, input().split()))
    print(solve(N, k, heights))

if __name__ == "__main__":
    main()

