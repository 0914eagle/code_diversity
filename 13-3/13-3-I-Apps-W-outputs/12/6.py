
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence of s and t
    lis = [1] * n
    lis_t = [1] * n
    # Loop through the string and find the longest non-decreasing subsequence
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and lis_t[i] < lis_t[j] + 1:
                lis_t[i] = lis_t[j] + 1
    # Find the maximum number of zeroes in t
    max_zeroes = 0
    for i in range(n):
        if s[i] == "0" and lis_t[i] > max_zeroes:
            max_zeroes = lis_t[i]
    # Create the output string t
    t = ["0"] * n
    for i in range(n):
        if s[i] == "0" and lis_t[i] == max_zeroes:
            t[i] = "1"
    return "".join(t)

