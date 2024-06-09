
import sys

def solve(R, W, d):
    # Initialize the number of ways to arrange the wine boxes
    ways = 1
    
    # Loop through each type of wine
    for i in range(2):
        # Get the number of boxes of the current type of wine
        num_boxes = R if i == 0 else W
        
        # Loop through each box of the current type of wine
        for j in range(num_boxes):
            # Check if the current box is the first box of a pile
            if j % d == 0:
                # Increment the number of ways to arrange the wine boxes
                ways += 1
    
    # Return the remainder of the number of ways to arrange the wine boxes divided by 10^9 + 7
    return ways % (10**9 + 7)

if __name__ == "__main__":
    R, W, d = map(int, input().split())
    print(solve(R, W, d))

