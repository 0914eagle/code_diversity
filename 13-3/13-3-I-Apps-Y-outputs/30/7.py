
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    current_height = 0

    # Iterate through the heights and check if the current height is greater than or equal to the required height
    for i in range(n):
        if heights[i] >= current_height:
            current_height = heights[i]
            min_operations += 1

    return min_operations

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_min_watering_operations(heights))

