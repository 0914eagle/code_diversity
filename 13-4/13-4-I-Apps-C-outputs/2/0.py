
import sys

def get_num_ways(r, w, d):
    # Base case: if there are no red or white wines, there is only one way to arrange them
    if r == 0 and w == 0:
        return 1
    
    # Base case: if there is only one type of wine, there is only one way to arrange them
    if r == 0 or w == 0:
        return 1
    
    # Initialize the number of ways to arrange the wines
    num_ways = 0
    
    # Iterate over the possible number of red wine piles
    for red_piles in range(1, r + 1):
        # Calculate the number of white wine piles
        white_piles = r - red_piles
        
        # Check if the number of red wine piles is valid
        if red_piles > d:
            continue
        
        # Calculate the number of ways to arrange the wines with the current number of red and white piles
        num_ways += get_num_ways(red_piles, white_piles, d)
    
    return num_ways % (10**9 + 7)

if __name__ == "__main__":
    r, w, d = map(int, sys.stdin.readline().split())
    print(get_num_ways(r, w, d))

