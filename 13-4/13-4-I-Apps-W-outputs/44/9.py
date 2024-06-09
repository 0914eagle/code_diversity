
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence of s and t
    lis = [1] * n
    lit = [1] * n
    # Loop through the string and find the longest non-decreasing subsequence
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                lit[i] = lit[j]
            elif s[i] >= s[j] and lis[i] == lis[j] + 1:
                lit[i] = lit[j]
    # Find the maximum number of zeroes in t
    max_zeroes = 0
    for i in range(n):
        if s[i] == "0":
            max_zeroes += 1
    # Initialize the string t with the same number of zeroes as s
    t = "0" * max_zeroes
    # Fill in the non-zero elements of t
    for i in range(n):
        if s[i] == "1":
            t = t[:i] + "1" + t[i:]
    return t

