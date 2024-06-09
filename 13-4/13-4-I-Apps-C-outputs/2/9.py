
import sys

def solve(R, W, d):
    # Initialize the number of ways to arrange the wine boxes
    ways = 1

    # Loop through each type of wine (red or white)
    for i in range(2):
        # Initialize the number of boxes of the current type of wine
        num_boxes = R if i == 0 else W

        # Loop through each box of the current type of wine
        for j in range(num_boxes):
            # If the current box is not the first box of its type,
            # then it can be placed in any position
            if j > 0:
                ways *= 2

            # If the current box is the first box of its type,
            # then it can be placed in either the first or second position
            else:
                ways *= 2
                if i == 0 and num_boxes - j > d:
                    ways -= 1

    # Return the remainder of the number of ways divided by 10^9 + 7
    return ways % (10**9 + 7)

if __name__ == '__main__':
    R, W, d = map(int, sys.stdin.readline().split())
    print(solve(R, W, d))

