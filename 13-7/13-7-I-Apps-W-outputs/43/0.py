
def solve(a, b, s):
    n = len(a)
    m = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            substring_a = a[i:j+1]
            for k in range(n):
                for l in range(k+1, n):
                    substring_b = b[k:l+1]
                    concatenated = substring_a + substring_b
                    if concatenated == s:
                        count += 1
    return count

