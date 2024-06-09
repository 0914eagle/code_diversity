
def solve(s, k):
    n = len(s)
    count = 0
    for i in range(n - k + 1):
        if s[i:i+k] == "RGB" * (k//3):
            count += 1
    return count
