
def f1(n, t):
    # Initialize a list to store the number of ways to choose s_i
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Iterate over the hops
    for i in range(1, n):
        # Initialize a set to store the unique values of s_i
        unique_s = set()
        
        # Iterate over the performers
        for j in range(1, n + 1):
            # If the performer is not in the same chair as before, add their new chair to the unique set
            if j != t[i - 1]:
                unique_s.add(j)
        
        # Update the number of ways to choose s_i by multiplying the number of unique values and the previous number of ways
        ways[i] = len(unique_s) * ways[i - 1]
    
    # Return the result modulo 10^9 + 7
    return ways[n] % 1000000007

def f2(n, t):
    # Initialize a list to store the number of ways to choose s_i
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Iterate over the hops
    for i in range(1, n):
        # Initialize a set to store the unique values of s_i
        unique_s = set()
        
        # Iterate over the performers
        for j in range(1, n + 1):
            # If the performer is not in the same chair as before, add their new chair to the unique set
            if j != t[i - 1]:
                unique_s.add(j)
        
        # Update the number of ways to choose s_i by multiplying the number of unique values and the previous number of ways
        ways[i] = len(unique_s) * ways[i - 1]
    
    # Return the result modulo 10^9 + 7
    return ways[n] % 1000000007

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f1(n, t))
    print(f2(n, t))

