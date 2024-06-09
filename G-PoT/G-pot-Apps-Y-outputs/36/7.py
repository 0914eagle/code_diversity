
def score_words(words):
    score = 0
    vowels = 'aeiouy'
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

# Input reading and function call
n = int(input())
words = input().split()
print(score_words(words))
