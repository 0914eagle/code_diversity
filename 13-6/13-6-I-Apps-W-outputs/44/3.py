
def get_beautiful_colorings(n):
    # Base case: Board of size 1x1 is either a single black tile or a single white tile
    if n == 1:
        return 2
    
    # Recursive case: Board of size nxn has 2^n beautiful colorings
    return 2 ** n

def get_suitable_colorings(n, k):
    # Base case: Board of size 1x1 is either a single black tile or a single white tile
    if n == 1:
        return 1
    
    # Recursive case: Board of size nxn has 2^n suitable colorings if k is at least n^2-1
    if k >= n**2-1:
        return 2 ** n
    
    # Recursive case: Board of size nxn has 0 suitable colorings if k is less than n^2-1
    return 0

def main():
    n, k = map(int, input().split())
    print(get_suitable_colorings(n, k) % 998244353)

if __name__ == '__main__':
    main()

