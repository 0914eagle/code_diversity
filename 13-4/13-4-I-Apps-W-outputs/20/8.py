
def solve(s, k):
    n = len(s)
    count = [0] * 26
    for i in range(n - k + 1):
        c = count[ord(s[i]) - ord('a')]
        count[ord(s[i]) - ord('a')] += 1
        if c == 0:
            count[ord(s[i + k - 1]) - ord('a')] -= 1
    for i in range(1, 26):
        count[i] += count[i - 1]
    return max(count)

