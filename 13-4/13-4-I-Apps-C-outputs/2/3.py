
import sys

def get_number_of_ways(r, w, d):
    # Base case: if there are no red or white wines, there is only one way to arrange them
    if r == 0 and w == 0:
        return 1
    
    # Base case: if there is only one type of wine, there is only one way to arrange them
    if r == 0 or w == 0:
        return 1
    
    # Recursive case: arrange the wines into piles
    total_ways = 0
    for i in range(1, min(d+1, r+1)):
        # Number of ways to arrange the red wines into piles of size i
        red_ways = get_number_of_ways(r-i, w, d)
        # Number of ways to arrange the white wines into piles of size i
        white_ways = get_number_of_ways(r, w-i, d)
        total_ways += red_ways * white_ways
    
    return total_ways

def main():
    r, w, d = map(int, sys.stdin.readline().split())
    print(get_number_of_ways(r, w, d) % (10**9 + 7))

if __name__ == "__main__":
    main()

