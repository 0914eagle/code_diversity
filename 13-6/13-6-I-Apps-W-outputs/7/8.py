
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
    num_balloons = int(input())
    heights = list(map(int, input().split()))
    print(get_min_arrows(heights))

if __name__ == '__main__':
    main()

