
def solve():
    s = input()
    t = input()

    # Initialize the minimum value of i as the length of s
    i = len(s)

    # Loop through each substring of s of length i
    for j in range(len(s)):
        # Check if t is a subsequence of the substring
        if is_subsequence(t, s[j:j+i]):
            # If it is, update the minimum value of i
            i = j
            break

    # If i is the length of s, then t is not a subsequence of any substring of s
    if i == len(s):
        print(-1)
    else:
        print(i)

def is_subsequence(t, s):
    # Initialize the index of t as 0
    i = 0

    # Loop through each character of s
    for j in range(len(s)):
        # If the current character of s is the same as the current character of t, update the index of t
        if s[j] == t[i]:
            i += 1

        # If the index of t has reached the end, return True
        if i == len(t):
            return True

    # If the index of t has not reached the end, return False
    return False

solve()

