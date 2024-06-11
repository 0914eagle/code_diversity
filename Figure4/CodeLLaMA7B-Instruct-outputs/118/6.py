

def get_closest_vowel(word):
    
    # Find the index of the last consonant in the word
    last_consonant_index = -1
    for i in range(len(word) - 1, -1, -1):
        if word[i].isalpha() and not word[i].islower():
            last_consonant_index = i
            break

    # If there is no consonant in the word, return an empty string
    if last_consonant_index == -1:
        return ""

    # Find the index of the first vowel after the last consonant
    first_vowel_index = -1
    for i in range(last_consonant_index + 1, len(word)):
        if word[i].isalpha() and word[i].islower():
            first_vowel_index = i
            break

    # If there is no vowel after the last consonant, return an empty string
    if first_vowel_index == -1:
        return ""

    # Return the vowel between the last consonant and the first vowel
    return word[last_consonant_index + 1 : first_vowel_index]


