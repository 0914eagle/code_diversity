def get_closest_vowel(word):
    
    # My and best solution
    vowels = 'aeiou'
    word = word.lower()
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            for j in range(i-1, 0, -1):
                if word[j] not in vowels:
                    return word[j]
    return ''

