
def get_min_arrows(N, heights):
    # Initialize variables
    arrows = 0
    current_height = 1

    # Iterate through the heights of the balloons
    for i in range(N):
        # If the current height is less than or equal to the height of the balloon, shoot an arrow
        if current_height <= heights[i]:
            arrows += 1
            current_height += 1

    # Return the minimum number of arrows needed to pop all the balloons
    return arrows

def main():
    # Read the number of balloons and their heights from stdin
    N = int(input())
    heights = list(map(int, input().split()))

    # Call the get_min_arrows function and print the result
    print(get_min_arrows(N, heights))

if __name__ == '__main__':
    main()

