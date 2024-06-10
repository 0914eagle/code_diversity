
def score_words(words):
    score = 0
    for word in words:
        vowels = 0
        for char in word:
            if char in "aeiouy":
                vowels += 1
        if vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

def main():
    n = int(input())
    words = input().split()
    print(score_words(words))

if __name__ == '__main__':
    main()

