
def solve(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    substrings.sort()
    return substrings[k-1]

