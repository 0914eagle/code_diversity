
import sys

def get_suitable_colorings(n, k):
    # Base case: If the board is of size 1x1, there is only one suitable coloring
    if n == 1:
        return 1
    
    # Initialize the number of suitable colorings to 0
    suitable_colorings = 0
    
    # Iterate over all possible colors (0 for white and 1 for black)
    for color in range(2):
        # Get the number of suitable colorings for the current color
        suitable_colorings += get_suitable_colorings(n-1, k)
    
    # Return the number of suitable colorings modulo 998244353
    return suitable_colorings % 998244353

def main():
    n, k = map(int, input().split())
    print(get_suitable_colorings(n, k))

if __name__ == '__main__':
    main()

