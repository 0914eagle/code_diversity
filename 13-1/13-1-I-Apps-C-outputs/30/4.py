
import math

def solve(N, k, heights):
    # Calculate the average height of the houses
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

def main():
    N, k = map(int, input().split())
    heights = list(map(float, input().split()))
    print(solve(N, k, heights))

if __name__ == "__main__":
    main()

