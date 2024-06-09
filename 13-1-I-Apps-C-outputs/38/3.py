
def solve(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "+":
            count += 1
        else:
            count -= 1
    return count

