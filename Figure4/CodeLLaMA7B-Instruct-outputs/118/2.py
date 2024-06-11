

def get_closest_vowel(word):
    
    # Find the index of the first vowel from the right
    first_vowel_index = len(word) - 1
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in "aeiou":
            first_vowel_index = i
            break

    # Find the index of the last consonant from the right
    last_consonant_index = len(word) - 1
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() not in "aeiou":
            last_consonant_index = i
            break

    # Check if the vowel is between two consonants
    if first_vowel_index < last_consonant_index:
        return word[first_vowel_index]
    else:
        return ""


