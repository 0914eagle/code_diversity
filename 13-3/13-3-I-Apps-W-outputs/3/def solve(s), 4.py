
def solve(s):
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = ""
    for i in range(len(s)):
        if s[i] in vowels:
            if i < len(s) - 1 and s[i] == s[i + 1] and s[i] != "e" and s[i] != "o":
                continue
            if result and result[-1] == s[i]:
                continue
            result += s[i]
    return result

