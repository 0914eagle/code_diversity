
def f1(n, k):
    # Initialize the number of ways as 1
    ways = 1
    
    # Iterate from 2 to n
    for i in range(2, n + 1):
        # If i is less than or equal to k, the penguin can walk to house number 1
        if i <= k:
            # Increment the number of ways by the number of ways to write the numbers on the plaques
            ways += f1(i - 1, k)
        # If i is greater than k, the penguin cannot walk to house number 1
        else:
            # Increment the number of ways by the number of ways to write the numbers on the plaques, but with the restriction that the first house cannot be 1
            ways += f1(i - 1, k - 1)
    
    # Return the number of ways modulo 1000000007
    return ways % 1000000007

def f2(n, k):
    # Initialize the number of ways as 0
    ways = 0
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # If i is less than or equal to k, the penguin can walk to house number 1
        if i <= k:
            # Increment the number of ways by the number of ways to write the numbers on the plaques
            ways += f2(i - 1, k)
        # If i is greater than k, the penguin cannot walk to house number 1
        else:
            # Increment the number of ways by the number of ways to write the numbers on the plaques, but with the restriction that the first house cannot be 1
            ways += f2(i - 1, k - 1)
    
    # Return the number of ways modulo 1000000007
    return ways % 1000000007

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(f1(n, k))

