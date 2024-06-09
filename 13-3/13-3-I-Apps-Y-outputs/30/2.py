
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    max_height = max(heights)

    # Loop through each height and check if it can be reached
    for i in range(n):
        if heights[i] < max_height:
            # Find the left and right indices that can reach the current height
            left_idx = i
            right_idx = i
            while left_idx >= 0 and heights[left_idx] >= heights[i]:
                left_idx -= 1
            while right_idx < n and heights[right_idx] >= heights[i]:
                right_idx += 1

            # Update the minimum number of operations
            min_operations += 1

            # Update the heights of the flowers in the range [left_idx, right_idx]
            for j in range(left_idx + 1, right_idx):
                heights[j] = heights[i] + 1

    return min_operations

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_min_watering_operations(heights))

