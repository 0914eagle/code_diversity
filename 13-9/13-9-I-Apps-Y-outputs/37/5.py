
def score_words(words):
    score = 0
    for word in words:
        vowels = 0
        for letter in word:
            if letter in 'aeiou':
                vowels += 1
        if vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

def main():
    num_words = int(input())
    words = []
    for _ in range(num_words):
        words.append(input())
    score = score_words(words)
    print(score)

if __name__ == '__main__':
    main()

