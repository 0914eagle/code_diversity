
def solve(s, t):
    # Replace all '?' characters with all possible letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(s)):
        if s[i] == '?':
            s = s[:i] + letters + s[i+1:]
    
    # Find all occurrences of string t in string s
    occurrences = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            occurrences.append(i)
    
    # Replace letters in string s with letters that don't intersect with any occurrence of string t
    for i in range(len(s)):
        if i in occurrences:
            continue
        for j in range(len(letters)):
            if s[i] == letters[j]:
                s = s[:i] + letters[j+1] + s[i+1:]
                break
    
    return s

