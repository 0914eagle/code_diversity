def get_closest_vowel(word):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in vowels:
            for j in range(i+1, len(word)):
                if word[j] not in vowels:
                    return word[j]
    return ""

if