
def read_input():
    N = int(input())
    h = list(map(int, input().split()))
    return N, h

def get_min_operations(h):
    # Initialize the minimum number of operations to 0
    min_operations = 0
    # Initialize the current height of the flowers to 0
    current_height = 0
    # Loop through the heights of the flowers
    for i in range(len(h)):
        # If the current height is less than the height of the current flower
        if current_height < h[i]:
            # Increment the minimum number of operations
            min_operations += 1
            # Set the current height to the height of the current flower
            current_height = h[i]
    return min_operations

def main():
    N, h = read_input()
    print(get_min_operations(h))

if __name__ == '__main__':
    main()

