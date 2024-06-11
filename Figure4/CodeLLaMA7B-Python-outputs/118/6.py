def get_closest_vowel(word):
    
    # My and best solution
    # O(n) time | O(1) space
    vowels = "aeiou"
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            for j in range(i-1, -1, -1):
                if word[j] not in vowels:
                    return word[i]
    return ""


