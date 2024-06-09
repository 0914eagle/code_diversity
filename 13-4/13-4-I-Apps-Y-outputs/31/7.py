
def solve(s):
    result = ""
    for i in range(len(s)):
        if s[i] == "<" and i > 0 and s[i-1] != "<":
            result = result[:-1]
        else:
            result += s[i]
    return result

