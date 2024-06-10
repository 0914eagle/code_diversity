
def score_words(words):
    score = 0
    for word in words:
        vowels = 0
        for letter in word:
            if letter in 'aeiouy':
                vowels += 1
        if vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

if __name__ == '__main__':
    n = int(input())
    words = input().split()
    score = score_words(words)
    print(score)

