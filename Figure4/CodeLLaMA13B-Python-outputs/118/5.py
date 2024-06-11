def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels:
            return word[i]
    return ""

if __name__ == '__main__':
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel