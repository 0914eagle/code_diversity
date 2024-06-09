
def solve(s):
    k = 1
    while k * len(s) % len(s) == 0:
        if all(s[i:] == s[:len(s) - i] for i in range(len(s))):
            return k
        k += 1
    return 0

