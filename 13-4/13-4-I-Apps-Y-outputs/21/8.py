
def get_min_operations(heights):
    # Initialize variables
    n = len(heights)
    operations = 0
    max_height = max(heights)

    # Loop through each flower and check if it can be watered
    for i in range(n):
        if heights[i] < max_height:
            # Find the left and right boundaries for the current flower
            left = max(i - max_height, 0)
            right = min(i + max_height, n - 1)

            # Increase the height of the flowers between the left and right boundaries
            for j in range(left, right + 1):
                heights[j] += 1

            # Update the number of operations
            operations += 1

    return operations

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_min_operations(heights))

if __name__ == '__main__':
    main()

