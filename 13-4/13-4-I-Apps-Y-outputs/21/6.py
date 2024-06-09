
def read_input():
    N = int(input())
    h = list(map(int, input().split()))
    return N, h

def f1(N, h):
    # Initialize the minimum number of watering operations to be infinite
    min_operations = float('inf')
    # Initialize the current height of each flower to be 0
    current_heights = [0] * (N + 1)
    # Loop through each flower and its height
    for i, height in enumerate(h, start=1):
        # If the current height of the flower is not equal to its desired height,
        # we need to perform a watering operation
        if current_heights[i] != height:
            # Find the range of flowers that need to be watered
            l = i
            r = i
            while l > 0 and current_heights[l - 1] == height:
                l -= 1
            while r <= N and current_heights[r + 1] == height:
                r += 1
            # Update the current heights of the flowers in the range
            for j in range(l, r + 1):
                current_heights[j] = height
            # Increment the number of watering operations
            min_operations += 1
    return min_operations

def f2(N, h):
    # Initialize the minimum number of watering operations to be infinite
    min_operations = float('inf')
    # Initialize the current height of each flower to be 0
    current_heights = [0] * (N + 1)
    # Loop through each flower and its height
    for i, height in enumerate(h, start=1):
        # If the current height of the flower is not equal to its desired height,
        # we need to perform a watering operation
        if current_heights[i] != height:
            # Find the range of flowers that need to be watered
            l = i
            r = i
            while l > 0 and current_heights[l - 1] == height:
                l -= 1
            while r <= N and current_heights[r + 1] == height:
                r += 1
            # Update the current heights of the flowers in the range
            for j in range(l, r + 1):
                current_heights[j] = height
            # Increment the number of watering operations
            min_operations += 1
    return min_operations

if __name__ == '__main__':
    N, h = read_input()
    print(f1(N, h))
    print(f2(N, h))

