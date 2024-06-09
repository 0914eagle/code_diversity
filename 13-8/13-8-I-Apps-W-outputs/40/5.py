
def solve(s, t):
    # Replace all question marks with all possible letters
    s = s.replace("?", "abcdefghijklmnopqrstuvwxyz")
    # Initialize a counter for the maximum number of occurrences
    max_occurrences = 0
    # Loop through all possible letters
    for letter in "abcdefghijklmnopqrstuvwxyz":
        # Replace all occurrences of letter in t with question marks
        t_temp = t.replace(letter, "?")
        # Count the number of occurrences of t in s
        occurrences = s.count(t_temp)
        # If the number of occurrences is greater than the current maximum, update the maximum
        if occurrences > max_occurrences:
            max_occurrences = occurrences
    return max_occurrences

