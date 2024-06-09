
def solve(s):
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = ""
    for i in range(len(s)):
        if s[i] in vowels:
            if i + 1 < len(s) and s[i + 1] == s[i] and (s[i] != "e" or s[i + 1] != "o" or i + 2 >= len(s) or s[i + 2] != s[i]):
                continue
            result += s[i]
    return result

