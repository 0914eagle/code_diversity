
def f1(n, k, s):
    # Initialize a dictionary to store the results of subproblems
    dp = {}
    
    # Base case: if k is 0, the total cost is 0
    dp[0] = 0
    
    # Iterate over the characters of the string
    for i in range(n):
        # Iterate over the possible sizes of the subsequence
        for j in range(k+1):
            # If the subsequence has size j, the total cost is the cost of the previous subsequence plus the cost of the current character
            if j > 0:
                dp[j] = min(dp[j], dp[j-1] + 1)
            # If the subsequence has size j-1, the total cost is the cost of the previous subsequence plus the cost of the current character
            if j < k:
                dp[j+1] = min(dp[j+1], dp[j] + 1)
    
    # If the total cost is less than or equal to k, it is possible to generate a set of size k, so return the total cost
    if dp[k] <= k:
        return dp[k]
    # Otherwise, it is not possible to generate a set of size k, so return -1
    else:
        return -1

def f2(n, k, s):
    # Initialize a set to store the generated substrings
    subsets = set()
    
    # Iterate over the characters of the string
    for i in range(n):
        # Generate all possible substrings of length i+1
        for j in range(i+1):
            # If the substring is not already in the set, add it to the set and increment the size of the set
            if s[j:i+1] not in subsets:
                subsets.add(s[j:i+1])
    
    # If the size of the set is equal to k, return the total cost
    if len(subsets) == k:
        return len(s) - k
    # Otherwise, return -1
    else:
        return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(f1(n, k, s))
    print(f2(n, k, s))

