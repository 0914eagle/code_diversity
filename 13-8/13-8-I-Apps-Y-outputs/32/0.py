
def solve(s):
    n = len(s)
    k = 1
    count = 0
    for i in range(n):
        if s[i] == "0":
            left = max(0, i-k)
            right = min(n-1, i+k)
            for j in range(left, right+1):
                if s[j] == "1":
                    break
            else:
                count += 1
    return count

