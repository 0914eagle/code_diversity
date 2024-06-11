def get_closest_vowel(word):
    
    # My and best way solution
    # O(n) time | O(1) space - where n is the length of the word
    vowels = "aeiou"
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels:
            return word[i]
    return ""


