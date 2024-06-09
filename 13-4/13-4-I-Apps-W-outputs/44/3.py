
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence for each index
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    # Find the maximum length of a non-decreasing subsequence
    max_len = max(lis)
    # Find the indices with the maximum length
    max_indices = [i for i in range(n) if lis[i] == max_len]
    # Create a new string with the maximum length and the same number of zeroes as the input string
    t = "0" * n
    for i in max_indices:
        t = t[:i] + "1" + t[i+1:]
    return t

