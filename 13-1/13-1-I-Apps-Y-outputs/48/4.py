
def count_substrings(s, k):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if all(c in k for c in s[i:j+1]):
                count += 1
    return count

