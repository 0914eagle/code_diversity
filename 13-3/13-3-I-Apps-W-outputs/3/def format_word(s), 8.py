
def format_word(s):
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = ""
    for i in range(len(s)):
        if s[i] in vowels:
            if i + 1 < len(s) and s[i + 1] == s[i] and (s[i] != "e" or s[i + 1] != "o" or i + 2 >= len(s) or s[i + 2] != s[i]):
                result += s[i]
            elif i + 1 < len(s) and s[i + 1] in vowels and s[i] != s[i + 1]:
                result += s[i] + s[i + 1]
            else:
                result += s[i]
        else:
            result += s[i]
    return result

