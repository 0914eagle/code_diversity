
import sys

def get_number_of_ways(R, W, d):
    # Base case: if there are no red or white wine boxes, there is only one way to arrange them
    if R == 0 and W == 0:
        return 1
    
    # Initialize the number of ways to arrange the wine boxes
    ways = 0
    
    # If there are red wine boxes, consider arranging them into piles
    if R > 0:
        # The number of ways to arrange the red wine boxes into piles is the number of ways to choose the number of red wine boxes in the first pile, times the number of ways to arrange the remaining red wine boxes into piles
        ways += (R + 1) * get_number_of_ways(R - d, W, d)
    
    # If there are white wine boxes, consider arranging them into piles
    if W > 0:
        # The number of ways to arrange the white wine boxes into piles is the number of ways to choose the number of white wine boxes in the first pile, times the number of ways to arrange the remaining white wine boxes into piles
        ways += (W + 1) * get_number_of_ways(R, W - 1, d)
    
    # Return the number of ways to arrange the wine boxes
    return ways

def main():
    R, W, d = map(int, input().split())
    print(get_number_of_ways(R, W, d) % (10**9 + 7))

if __name__ == "__main__":
    main()

