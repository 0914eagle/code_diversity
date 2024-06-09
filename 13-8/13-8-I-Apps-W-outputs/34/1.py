
def solve(s):
    n = len(s)
    for k in range(1, n+1):
        # Iterate through all possible values of k
        # and check if the resulting string is lexicographically smallest
        result = ""
        for i in range(0, n-k+1):
            # Reverse the substring s[i:i+k-1]
            result += s[i+k-1:i-1:-1]
        if result < s:
            # If the resulting string is lexicographically smallest, return k and the result
            return k, result
    # If no such k exists, return -1 and the original string
    return -1, s

