
def prettiness(s):
    vowels = set("AEIOUY")
    simple_prettiness = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            substring = s[i:j]
            simple_prettiness += len([c for c in substring if c in vowels]) / len(substring)
    return simple_prettiness

