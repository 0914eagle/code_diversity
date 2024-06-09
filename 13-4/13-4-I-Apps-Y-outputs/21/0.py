
def read_input():
    N = int(input())
    h = list(map(int, input().split()))
    return N, h

def get_min_watering_operations(h):
    # Initialize the minimum number of watering operations required to be N
    min_operations = N
    # Initialize the current height of each flower to be 0
    current_height = [0] * N
    # Loop through each flower and its height
    for i, height in enumerate(h):
        # If the current height of the flower is less than its target height,
        # we need to perform watering operations to increase its height
        if current_height[i] < height:
            # Calculate the number of watering operations required to increase the height of the flower to its target height
            operations = height - current_height[i]
            # Update the minimum number of watering operations required if the current number of operations is less than the minimum
            min_operations = min(min_operations, operations)
        # Update the current height of the flower to be its target height
        current_height[i] = height
    return min_operations

def main():
    N, h = read_input()
    print(get_min_watering_operations(h))

if __name__ == '__main__':
    main()

