

def get_closest_vowel(word):
    
    # Find the index of the first vowel from the right
    first_vowel_index = len(word) - 1
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in "aeiou":
            first_vowel_index = i
            break

    # Find the index of the last vowel from the right
    last_vowel_index = len(word) - 1
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in "aeiou":
            last_vowel_index = i
            break

    # Check if the first vowel is the last vowel
    if first_vowel_index == last_vowel_index:
        return ""

    # Find the index of the closest vowel
    closest_vowel_index = -1
    for i in range(first_vowel_index + 1, last_vowel_index):
        if word[i].lower() in "aeiou":
            closest_vowel_index = i
            break

    # Return the closest vowel
    if closest_vowel_index == -1:
        return ""
    else:
        return word[closest_vowel_index]


