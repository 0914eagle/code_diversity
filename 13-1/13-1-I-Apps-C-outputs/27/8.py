
def f1(n, k):
    # Initialize the number of ways to write the numbers on the houses' plaques
    num_ways = 1
    
    # Iterate over the houses
    for i in range(1, n + 1):
        # If the house is not the first house
        if i != 1:
            # If the house is indexed from 1 to k, inclusive
            if i <= k:
                # The penguin can walk to house number 1
                num_ways *= 1
            else:
                # The penguin cannot walk to house number 1
                num_ways *= 0
        else:
            # The penguin can get back to house number 1 after some non-zero number of walks from a house to a house
            num_ways *= 1
    
    # Return the number of ways modulo 1000000007 (10^9 + 7)
    return num_ways % 1000000007

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(f1(n, k))

