
import sys

def get_suitable_colorings(n, k):
    # Base case: If the board is of size 1x1, there is only one suitable coloring
    if n == 1:
        return 1
    
    # Initialize the number of suitable colorings to 0
    suitable_colorings = 0
    
    # Iterate over all possible colors (white and black)
    for color in ['W', 'B']:
        # Get the number of suitable colorings for the current color
        suitable_colorings += get_suitable_colorings_helper(n-1, k, color)
    
    # Return the total number of suitable colorings
    return suitable_colorings

def get_suitable_colorings_helper(n, k, color):
    # Base case: If the board is of size 1x1, there is only one suitable coloring
    if n == 1:
        return 1
    
    # Initialize the number of suitable colorings to 0
    suitable_colorings = 0
    
    # Iterate over all possible colors for the next row
    for next_color in ['W', 'B']:
        # If the next color is the same as the current color, increment the number of suitable colorings
        if next_color == color:
            suitable_colorings += 1
        # If the next color is different from the current color, increment the number of suitable colorings by the number of suitable colorings for the next row
        else:
            suitable_colorings += get_suitable_colorings_helper(n-1, k, next_color)
    
    # Return the total number of suitable colorings
    return suitable_colorings

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_suitable_colorings(n, k) % 998244353)

