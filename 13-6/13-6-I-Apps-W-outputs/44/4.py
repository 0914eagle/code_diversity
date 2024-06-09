
def get_beautiful_colorings(n):
    # Base case: Board of size 1x1 is either a single black tile or a single white tile
    if n == 1:
        return 2
    
    # Recursive case: Board of size nxn has (n-1)x(n-1) sub-boards
    # Count the number of beautiful colorings in each sub-board and multiply by 2 (for white and black tiles)
    return (get_beautiful_colorings(n-1) * 2) ** 2

def get_suitable_colorings(n, k):
    # Base case: Board of size 1x1 is either a single black tile or a single white tile
    if n == 1:
        return 1
    
    # Recursive case: Board of size nxn has (n-1)x(n-1) sub-boards
    # Count the number of suitable colorings in each sub-board and multiply by 2 (for white and black tiles)
    return (get_suitable_colorings(n-1, k) * 2) ** 2

def count_suitable_colorings(n, k):
    # Get the number of beautiful colorings of the board
    beautiful_colorings = get_beautiful_colorings(n)
    
    # Get the number of suitable colorings of the board
    suitable_colorings = get_suitable_colorings(n, k)
    
    # Return the number of suitable colorings modulo 998244353
    return suitable_colorings % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(count_suitable_colorings(n, k))

