

def get_closest_vowel(word):
    
    # Find the index of the last consonant in the word
    last_consonant_index = len(word) - 1
    while last_consonant_index >= 0 and word[last_consonant_index].isalpha() and not word[last_consonant_index].islower():
        last_consonant_index -= 1

    # If there are no consonants in the word, return an empty string
    if last_consonant_index == -1:
        return ""

    # Find the index of the first consonant after the last consonant
    first_consonant_index = last_consonant_index + 1
    while first_consonant_index < len(word) and word[first_consonant_index].isalpha() and not word[first_consonant_index].islower():
        first_consonant_index += 1

    # If there are no consonants after the last consonant, return an empty string
    if first_consonant_index == len(word):
        return ""

    # Return the vowel that is between the last consonant and the first consonant
    vowel_index = first_consonant_index - 1
    while vowel_index >= 0 and not word[vowel_index].islower():
        if word[vowel_index].isalpha() and word[vowel_index].islower():
            return word[vowel_index]
        vowel_index -= 1

    return ""


