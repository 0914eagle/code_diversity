
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    current_heights = [0] * n

    # Loop through each height and check if it needs to be increased
    for i in range(n):
        if heights[i] > current_heights[i]:
            # Increase the height of all flowers between the current height and the target height
            for j in range(current_heights[i], heights[i]):
                min_operations += 1
                current_heights[i] = j

    return min_operations

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_min_watering_operations(heights))

if __name__ == '__main__':
    main()

