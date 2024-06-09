
def get_prettiness(title):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    prettiness = 0
    for i in range(len(title)):
        for j in range(i, len(title) + 1):
            substring = title[i:j]
            vowel_count = 0
            for char in substring:
                if char in vowels:
                    vowel_count += 1
            prettiness += vowel_count / len(substring)
    return prettiness

