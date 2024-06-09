
def prettiness(s):
    vowels = ["I", "E", "A", "O", "U", "Y"]
    vowel_count = 0
    for c in s:
        if c in vowels:
            vowel_count += 1
    return vowel_count / len(s)

