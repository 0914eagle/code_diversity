
def is_easily_playable(s):
    # Check if the length of the string is between 1 and 100 (inclusive)
    if not 1 <= len(s) <= 100:
        return "No"

    # Check if all characters are L, R, U, or D
    for c in s:
        if c not in "LRUDD":
            return "No"

    # Check if every character in an odd position is R, U, or D
    for i in range(1, len(s), 2):
        if s[i] not in "RUD":
            return "No"

    # Check if every character in an even position is L, U, or D
    for i in range(2, len(s), 2):
        if s[i] not in "LUD":
            return "No"

    return "Yes"

