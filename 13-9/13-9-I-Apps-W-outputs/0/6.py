
def solve(s):
    # Initialize a set to store the unique strings
    strings = set()

    # Iterate over the input string
    for i in range(len(s)):
        # Check if the current character is 'w' or 'm'
        if s[i] in ['w', 'm']:
            # If it is, skip it and continue to the next character
            continue
        # If it is not, create a new string by replacing 'w' and 'm' with 'u' and 'n' respectively
        new_string = s[:i] + s[i].replace('w', 'u').replace('m', 'n') + s[i+1:]
        # Add the new string to the set
        strings.add(new_string)

    # Return the number of unique strings modulo 10^9+7
    return len(strings) % (10**9+7)

