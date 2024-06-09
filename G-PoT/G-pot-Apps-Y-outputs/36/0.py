
def score_words(words):
    score = 0
    vowels = 'aeiouy'
    
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

# Input reading and function call
n = int(input())
words = input().split()
print(score_words(words))
