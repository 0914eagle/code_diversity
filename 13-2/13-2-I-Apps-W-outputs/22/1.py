
def solve():
    s = input()
    t = input()

    # Initialize the minimum value of i as the length of s
    min_i = len(s)

    # Loop through all possible values of i
    for i in range(len(s)):
        # Check if t is a subsequence of the first i characters of s'
        if is_subsequence(t, s * 100000000000000000)[0:i]:
            # If it is, update the minimum value of i
            min_i = min(min_i, i)

    # If no value of i satisfies the condition, return -1
    if min_i == len(s):
        return -1
    else:
        return min_i

# Check if t is a subsequence of s
def is_subsequence(t, s):
    i, j = 0, 0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            i += 1
        j += 1
    return i == len(t)

print(solve())

