
def solve(a, s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            product = int(s[i]) * int(s[j])
            if product == a:
                count += 1
    return count

