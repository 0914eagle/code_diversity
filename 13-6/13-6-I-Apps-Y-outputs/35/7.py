
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Loop through the prefixes and suffixes and add them to the dictionary
    for i in range(len(prefixes)):
        prefix_suffixes[prefixes[i]] = "P"
        prefix_suffixes[suffixes[i]] = "S"

    # Initialize an empty string to store the result
    result = ""

    # Loop through the dictionary and check if the value is "P" or "S"
    for i in range(n):
        if prefix_suffixes[s[i]] == "P":
            result += "P"
        else:
            result += "S"

    return result

