
def score_words(words):
    score = 0
    for word in words:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        vowel_count = 0
        for char in word:
            if char in vowels:
                vowel_count += 1
        if vowel_count % 2 == 0:
            score += 2
        else:
            score += 1
    return score

def main():
    n = int(input())
    words = input().split()
    score = score_words(words)
    print(score)

if __name__ == '__main__':
    main()

