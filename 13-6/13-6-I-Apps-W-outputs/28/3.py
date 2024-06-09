
def solve(s, t):
    # Replace all '?' characters with all possible letters
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] == '?':
            s = s[:i] + letters + s[i+1:]
    # Calculate the suitability of the string
    suitability = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            suitability += 1
    return s

