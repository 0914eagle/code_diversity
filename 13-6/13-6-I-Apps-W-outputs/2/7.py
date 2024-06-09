
def solve(n, s):
    # Initialize the number of sets to 0
    sets = 0

    # Iterate over the string s
    for i in range(n):
        # If the current character is 0 or 1, increment the number of sets
        if s[i] in "01":
            sets += 1
        # If the current character is ? and the previous character is 0 or 1, decrement the number of sets
        elif s[i] == "?" and (i == 0 or s[i-1] in "01"):
            sets -= 1

    # Return the number of sets
    return sets

