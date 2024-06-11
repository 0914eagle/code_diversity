def get_closest_vowel(word):
    
    # My and best way solution
    # O(n) time | O(1) space - where n is the length of the word
    vowels = "aeiou"
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels:
            if word[i - 1] in vowels:
                continue
            if word[i + 1] in vowels:
                continue
            return word[i]
    return ""


