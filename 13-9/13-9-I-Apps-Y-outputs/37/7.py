
def score_words(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    score = 0
    for word in words:
        vowel_count = 0
        for letter in word:
            if letter in vowels:
                vowel_count += 1
        if vowel_count % 2 == 0:
            score += 2
        else:
            score += 1
    return score

