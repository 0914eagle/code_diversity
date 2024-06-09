
def get_min_string(s, k):
    n = len(s)
    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            if s[i] > s[j]:
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                k -= 1
                if k == 0:
                    break
        if k == 0:
            break
    return s

