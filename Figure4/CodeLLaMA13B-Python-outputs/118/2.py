def get_closest_vowel(word):
    
    vowels = "aeiouAEIOU"
    word = word[::-1]
    for i, char in enumerate(word):
        if char in vowels and word[i-1] not in vowels:
            return char
    return ""


if __name__ == '