
def solve(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if substring not in substrings:
                substrings.append(substring)
    
    substrings.sort()
    return substrings[k-1]

