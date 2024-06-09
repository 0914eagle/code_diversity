
import sys

def get_number_of_ways(R, W, d):
    # Base case: if there are no red or white wine boxes, there is only one way to arrange them
    if R == 0 and W == 0:
        return 1
    
    # Initialize the number of ways to arrange the wine boxes
    number_of_ways = 0
    
    # If there are red wine boxes, consider arranging them first
    if R > 0:
        # Get the number of ways to arrange the red wine boxes
        number_of_ways += get_number_of_ways(R-1, W, d)
    
    # If there are white wine boxes, consider arranging them next
    if W > 0:
        # Get the number of ways to arrange the white wine boxes
        number_of_ways += get_number_of_ways(R, W-1, d)
    
    # If there are both red and white wine boxes, consider arranging them together
    if R > 0 and W > 0:
        # Get the number of ways to arrange the red and white wine boxes together
        number_of_ways += get_number_of_ways(R-1, W-1, d)
    
    return number_of_ways

def main():
    R, W, d = map(int, input().split())
    print(get_number_of_ways(R, W, d) % (10**9 + 7))

if __name__ == "__main__":
    main()

