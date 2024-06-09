
def is_haiku(phrase_1, phrase_2, phrase_3):
    # Check if the sum of the syllables in each phrase is 17, which is the required number of syllables in a Haiku
    if phrase_1 + phrase_2 + phrase_3 != 17:
        return "NO"
    
    # Check if the number of syllables in each phrase is within the required range
    if not (1 <= phrase_1 <= 5 and 1 <= phrase_2 <= 5 and 1 <= phrase_3 <= 7):
        return "NO"
    
    # Check if the phrases can be arranged to form a Haiku
    if phrase_1 == 5 and phrase_2 == 5 and phrase_3 == 7:
        return "YES"
    elif phrase_1 == 5 and phrase_2 == 7 and phrase_3 == 5:
        return "YES"
    elif phrase_1 == 7 and phrase_2 == 5 and phrase_3 == 5:
        return "YES"
    else:
        return "NO"

