def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ""

if __name__ == "__main__":
    print(get_closest_vowel("y