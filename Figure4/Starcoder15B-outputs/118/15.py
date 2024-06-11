def get_closest_vowel(word):
    
    vowels = 'aeiou'
    vowel_list = []
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            vowel_list.append(word[i])
        elif word[i] not in vowels and len(vowel_list) > 0:
            return vowel_list[-1]
    return ''

