
def solve(s, t):
    # Replace all '?' characters with all possible lowercase letters
    s = s.replace("?", "abcdefghijklmnopqrstuvwxyz")
    # Initialize a list to store the suitability of each string
    suitabilities = []
    # Iterate over each possible string
    for i in range(len(s)):
        # Calculate the suitability of the current string
        suitability = 0
        for j in range(len(t)):
            # If the current string contains the j-th character of t
            if s[i+j] == t[j]:
                # Increment the suitability
                suitability += 1
        # Add the suitability of the current string to the list
        suitabilities.append(suitability)
    # Return the string with the highest suitability
    return s[suitabilities.index(max(suitabilities))]

