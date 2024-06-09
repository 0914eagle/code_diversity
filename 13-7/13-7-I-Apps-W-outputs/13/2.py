
def get_prettiness(title):
    vowels = ["I", "E", "A", "O", "U", "Y"]
    title_length = len(title)
    simple_prettiness = 0
    for i in range(title_length):
        for j in range(i, title_length + 1):
            substring = title[i:j]
            vowel_count = 0
            for char in substring:
                if char in vowels:
                    vowel_count += 1
            simple_prettiness += vowel_count / len(substring)
    return simple_prettiness

