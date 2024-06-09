
def get_typo_words(s, t):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            w = s[:i] + s[j:]
            if w == t:
                count += 1
    return count

