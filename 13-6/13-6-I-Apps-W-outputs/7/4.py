
def get_min_arrows(heights):
    # Initialize variables
    min_arrows = 0
    current_height = 1

    # Iterate through the heights of the balloons
    for height in heights:
        # If the current height is less than or equal to the height of the balloon, we need to shoot an arrow
        if current_height <= height:
            min_arrows += 1
            current_height += 1

    return min_arrows

def main():
    # Read the number of balloons and their heights from stdin
    num_balloons = int(input())
    balloon_heights = list(map(int, input().split()))

    # Call the get_min_arrows function and print the result
    print(get_min_arrows(balloon_heights))

if __name__ == '__main__':
    main()

