
def score_words(words):
    vowels = 'aeiouy'
    score = 0
    for word in words:
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
        if count % 2 == 0:
            score += 2
        else:
            score += 1
    return score

n = int(input())
words = input().split()
print(score_words(words))
