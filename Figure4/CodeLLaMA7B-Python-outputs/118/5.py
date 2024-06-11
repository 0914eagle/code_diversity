def get_closest_vowel(word):
    
    vowels = "aeiou"
    word = word.lower()
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i-1] in vowels:
                continue
            if word[i+1] in vowels:
                continue
            return word[i]
    return ""


if __name__ == "__main__":
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel("FULL"))
    print(get_closest_vowel("quick"))
    print(get_closest_vowel("ab