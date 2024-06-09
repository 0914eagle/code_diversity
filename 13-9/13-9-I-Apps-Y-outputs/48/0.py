
def is_haiku(phrase_1, phrase_2, phrase_3):
    # Check if the sum of the syllables in each phrase is 17
    if phrase_1 + phrase_2 + phrase_3 == 17:
        # Check if the number of syllables in each phrase is valid
        if phrase_1 in range(1, 6) and phrase_2 in range(1, 6) and phrase_3 in range(1, 8):
            return "YES"
    return "NO"

