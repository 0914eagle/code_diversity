
import sys

def get_number_of_ways(r, w, d):
    # Base case: if there are no red or white wines, there is only one way to arrange them
    if r == 0 and w == 0:
        return 1
    
    # Base case: if there is only one type of wine, there is only one way to arrange them
    if r == 0 or w == 0:
        return 1
    
    # Initialize the number of ways to arrange the wines
    number_of_ways = 0
    
    # Iterate over the possible number of red wine piles
    for i in range(1, r + 1):
        # Get the number of ways to arrange the remaining wines
        remaining_ways = get_number_of_ways(r - i, w, d)
        
        # If the number of ways is 0, continue to the next iteration
        if remaining_ways == 0:
            continue
        
        # If the number of red wine piles is less than or equal to the maximum number of red wine piles allowed, add the number of ways to the total
        if i <= d:
            number_of_ways += remaining_ways
    
    return number_of_ways

def main():
    r, w, d = map(int, input().split())
    print(get_number_of_ways(r, w, d) % (10**9 + 7))

if __name__ == "__main__":
    main()

