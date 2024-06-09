
def solve(n, m, a, b, s):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            substring_a = a[i:j+1]
            for k in range(n):
                for l in range(k+1, n):
                    substring_b = b[k:l+1]
                    concat = substring_a + substring_b
                    if concat == s and i <= k <= j and k <= l <= j:
                        count += 1
    return count

