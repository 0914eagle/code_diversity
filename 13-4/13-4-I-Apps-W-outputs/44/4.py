
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence array
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    # Find the maximum length of the longest non-decreasing subsequence
    max_len = max(lis)
    # Initialize the binary string with all zeros
    t = "0" * n
    # Fill in the ones in the binary string
    for i in range(n):
        if lis[i] == max_len:
            t = t[:i] + "1" + t[i+1:]
    return t

