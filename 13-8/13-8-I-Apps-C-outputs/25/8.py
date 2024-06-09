
import sys

def solve(R, W, d):
    # Calculate the number of ways to arrange the red and white wine piles
    num_red_piles = (R + d - 1) // d
    num_white_piles = W
    num_piles = num_red_piles + num_white_piles
    
    # Calculate the number of ways to arrange the piles in a line
    num_arrangements = 1
    for i in range(num_piles):
        num_arrangements *= num_piles - i
    
    # Calculate the number of ways to arrange the red and white wine piles in a line with no two piles of the same type next to each other
    num_arrangements_with_no_adjacent_piles = 0
    for i in range(num_red_piles):
        for j in range(i + 1, num_red_piles):
            num_arrangements_with_no_adjacent_piles += num_white_piles
    
    # Calculate the number of ways to arrange the piles in a line with no two piles of the same type next to each other and no red pile with more than d boxes
    num_valid_arrangements = num_arrangements_with_no_adjacent_piles - num_red_piles + 1
    
    # Return the number of valid arrangements modulo 10^9 + 7
    return num_valid_arrangements % (10**9 + 7)

if __name__ == "__main__":
    R, W, d = map(int, sys.stdin.readline().split())
    print(solve(R, W, d))

