
def get_lexicographically_smallest_string_and_k(s):
    n = len(s)
    for k in range(1, n+1):
        s_modified = s[:k]
        for i in range(n-k+1):
            s_modified += s[i+k-1] + s[i:i+k-1][::-1]
        if s_modified < s:
            return s_modified, k
    return s, 1

