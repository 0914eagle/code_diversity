
def solve(s):
    # Initialize a set to store the possible strings
    strings = set()

    # Iterate over the letters in the input string
    for i in range(len(s)):
        # If the letter is 'w', add "uu" to the set of strings
        if s[i] == 'w':
            strings.add("uu")
        # If the letter is 'm', add "nn" to the set of strings
        elif s[i] == 'm':
            strings.add("nn")
        # If the letter is not 'w' or 'm', add the letter itself to the set of strings
        else:
            strings.add(s[i])

    # Return the number of strings in the set, modulo 10^9+7
    return len(strings) % 1000000007

