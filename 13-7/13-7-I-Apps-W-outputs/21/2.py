
def solve(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j - i + 1 >= 4 and "bear" in s[i:j+1]:
                count += 1
    return count

