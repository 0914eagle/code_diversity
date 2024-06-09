
def solve():
    s = input()
    t = input()

    # Initialize the minimum value of i as the length of s
    min_i = len(s)

    # Loop through each possible value of i
    for i in range(len(s), 0, -1):
        # Check if t is a subsequence of the first i characters of s'
        if is_subsequence(t, s * 100)[:i]:
            # If it is, update the minimum value of i
            min_i = i
            break

    # Print the minimum value of i
    print(min_i)

def is_subsequence(s, t):
    # Initialize the index of the first character in s
    i = 0

    # Loop through each character in t
    for c in t:
        # If the current character in t is in s, update the index of the first character in s
        if c in s[i:]:
            i = s.index(c) + 1
        # If the current character in t is not in s, return False
        else:
            return False

    # If we reach the end of t, return True
    return True

solve()

