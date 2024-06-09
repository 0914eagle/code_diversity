
def solve(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] == "bear":
                count += 1
    return count

