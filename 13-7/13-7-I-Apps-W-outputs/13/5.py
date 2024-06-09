
def get_prettiness(title):
    vowels = ["I", "E", "A", "O", "U", "Y"]
    vowel_count = 0
    for char in title:
        if char in vowels:
            vowel_count += 1
    return vowel_count / len(title)

