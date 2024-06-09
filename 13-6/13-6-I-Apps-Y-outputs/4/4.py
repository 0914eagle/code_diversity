
def solve(s, k):
    n = len(s)
    count = 0
    for i in range(n - k + 1):
        substring = s[i:i+k]
        if "RGB" in substring:
            count += 1
    return count

