
def is_easily_playable(S):
    # Check if the length of the string is between 1 and 100 (inclusive)
    if not 1 <= len(S) <= 100:
        return "No"
    
    # Check if the string contains only the allowed characters (L, R, U, D)
    if not all(c in ["L", "R", "U", "D"] for c in S):
        return "No"
    
    # Check if the string satisfies the given conditions
    if all(c in ["R", "U", "D"] if i % 2 == 1 else c in ["L", "U", "D"] if i % 2 == 0 for i, c in enumerate(S)):
        return "Yes"
    
    return "No"

