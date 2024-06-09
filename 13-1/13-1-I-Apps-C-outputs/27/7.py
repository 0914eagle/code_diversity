
def f1(n, k):
    # Initialize the number of ways to write the numbers on the houses' plaques
    ways = 1
    
    # Iterate over the houses
    for i in range(1, n + 1):
        # If the house is indexed from 1 to k, inclusive, it can walk to house number 1
        if i <= k:
            ways *= 2
        # If the house is indexed from k + 1 to n, inclusive, it definitely cannot walk to house number 1
        else:
            ways *= 1
    
    # Return the number of ways modulo 1000000007 (10^9 + 7)
    return ways % 1000000007

def f2(n, k):
    # Initialize the number of ways to write the numbers on the houses' plaques
    ways = 1
    
    # Iterate over the houses
    for i in range(1, n + 1):
        # If the house is indexed from 1 to k, inclusive, it can walk to house number 1
        if i <= k:
            ways *= 2
        # If the house is indexed from k + 1 to n, inclusive, it definitely cannot walk to house number 1
        else:
            ways *= 1
    
    # Return the number of ways modulo 1000000007 (10^9 + 7)
    return ways % 1000000007

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(f1(n, k))
    print(f2(n, k))

