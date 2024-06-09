
def solve(s1, s2, t):
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            break
    else:
        return "-1"
    s3 = list(s1)
    for j in range(i+1, n):
        if s1[j] != s2[j]:
            break
    s3[i] = s2[j]
    s3[j] = s1[i]
    if f(s1, "".join(s3)) == t and f(s2, "".join(s3)) == t:
        return "".join(s3)
    return "-1"

def f(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

