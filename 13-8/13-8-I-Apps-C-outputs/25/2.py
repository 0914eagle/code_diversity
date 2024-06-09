
import sys

def get_number_of_ways(R, W, d):
    # Base case: if there are no red wine boxes, return 1
    if R == 0:
        return 1
    
    # Initialize the number of ways to arrange the wine boxes
    number_of_ways = 0
    
    # Iterate over the possible number of red wine boxes in the first pile
    for i in range(1, min(d + 1, R + 1)):
        # Recursively call the function to get the number of ways to arrange the remaining wine boxes
        number_of_ways += get_number_of_ways(R - i, W, d)
    
    # Return the number of ways to arrange the wine boxes
    return number_of_ways

def main():
    R, W, d = map(int, input().split())
    print(get_number_of_ways(R, W, d) % (10**9 + 7))

if __name__ == "__main__":
    main()

