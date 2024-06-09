
def solve(s, t):
    # Replace '?' characters with all possible letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(s)):
        if s[i] == '?':
            for letter in letters:
                s = s[:i] + letter + s[i+1:]
    # Calculate suitability of string s
    suitability = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            suitability += 1
    # Return string s with maximal suitability
    return s

