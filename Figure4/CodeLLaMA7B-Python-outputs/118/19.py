def get_closest_vowel(word):
    
    # My and best way solution
    # O(n) time | O(1) space - where n is the length of the word
    vowels = "aeiou"
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            for j in range(i + 1, len(word) - 1):
                if word[j] in vowels:
                    return word[i]
    return ""

