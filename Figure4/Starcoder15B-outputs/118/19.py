def get_closest_vowel(word):
    
    vowels = 'aeiou'
    word = word.lower()
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] not in vowels:
            for j in range(i-1, -1, -1):
                if word[j] in vowels:
                    return word[j]
                else:
                    continue
    return ''

