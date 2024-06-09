
def solve(s):
    result = ""
    for i in range(len(s)):
        if s[i] != "<":
            result += s[i]
        elif i > 0 and s[i-1] != "<":
            result = result[:-1]
    return result

