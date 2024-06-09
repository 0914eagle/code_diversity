
def is_haiku(a, b, c):
    # Check if the sum of the syllables is divisible by 3
    if a + b + c % 3 != 0:
        return "NO"
    
    # Check if the syllable counts are valid
    if a not in range(1, 11) or b not in range(1, 11) or c not in range(1, 11):
        return "NO"
    
    # Check if the syllable counts are in the correct order
    if a == 5 and b == 7 and c == 5:
        return "YES"
    else:
        return "NO"

