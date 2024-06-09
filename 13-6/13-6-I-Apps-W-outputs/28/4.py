
def suitability(s, t):
    # Replace all '?' characters with all possible letters
    s = s.replace("?", "abcdefghijklmnopqrstuvwxyz")
    # Initialize suitability score to 0
    score = 0
    # Loop through all positions in s
    for i in range(len(s)):
        # If the letter at the current position is not '?', skip to the next position
        if s[i] != "?":
            continue
        # If the letter at the current position is '?', replace it with all possible letters
        s = s[:i] + "abcdefghijklmnopqrstuvwxyz" + s[i+1:]
        # Increment suitability score by the number of non-intersecting occurrences of t in s
        score += s.count(t)
    # Return the suitability score
    return score

