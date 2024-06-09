
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
    # Find the starting index of the longest non-decreasing subsequence
    start_index = lis.index(max_len)
    # Find the ending index of the longest non-decreasing subsequence
    end_index = start_index + max_len - 1
    # Create a new string with the maximum number of zeroes
    t = "0" * max_len
    # Fill in the non-zero elements of the string
    for i in range(start_index, end_index + 1):
        if s[i] == "1":
            t = t[:i - start_index] + "1" + t[i - start_index + 1:]
    return t

