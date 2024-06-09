
def is_easily_playable(S):
    # Check if the length of the string is between 1 and 100 (inclusive)
    if not 1 <= len(S) <= 100:
        return "No"

    # Check if the string contains only the allowed characters (L, R, U, D)
    if not all(c in ["L", "R", "U", "D"] for c in S):
        return "No"

    # Check if the characters in odd positions are R, U, or D
    if not all(S[i] in ["R", "U", "D"] for i in range(1, len(S), 2)):
        return "No"

    # Check if the characters in even positions are L, U, or D
    if not all(S[i] in ["L", "U", "D"] for i in range(2, len(S), 2)):
        return "No"

    return "Yes"

