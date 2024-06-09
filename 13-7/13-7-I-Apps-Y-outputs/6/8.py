
def is_easily_playable(s):
    # Check if the length of the string is between 1 and 100 inclusive
    if not 1 <= len(s) <= 100:
        return "No"

    # Check if all characters are L, R, U, or D
    for c in s:
        if c not in "LRULD":
            return "No"

    # Check if all characters in odd positions are R, U, or D
    for i in range(1, len(s), 2):
        if s[i] not in "RUD":
            return "No"

    # Check if all characters in even positions are L, U, or D
    for i in range(2, len(s), 2):
        if s[i] not in "LUD":
            return "No"

    # If all conditions are met, return "Yes"
    return "Yes"

