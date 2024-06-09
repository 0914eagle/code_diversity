
def solve(s):
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = ""
    for i in range(len(s)):
        if s[i] in vowels:
            if i + 1 < len(s) and s[i + 1] == s[i]:
                if s[i] in ["e", "o"] and i + 2 < len(s) and s[i + 2] == s[i]:
                    result += s[i]
                    i += 2
                else:
                    result += s[i]
                    i += 1
            else:
                result += s[i]
        else:
            result += s[i]
    return result

