
def solve(s, t):
    # Replace '?' characters with all possible lowercase letters
    s = s.replace("?", "abcdefghijklmnopqrstuvwxyz")
    # Initialize suitability variable
    suitability = 0
    # Loop through all possible combinations of letters
    for i in range(len(s) - len(t) + 1):
        # Check if the current combination forms a valid string
        if s[i:i+len(t)] == t:
            # If it does, update the suitability variable
            suitability = max(suitability, 1)
    # Return the string with the highest suitability
    return s

