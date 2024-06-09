
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Loop through the prefixes and suffixes and add them to the dictionary
    for i in range(len(prefixes)):
        prefix_suffixes[prefixes[i]] = "P"
        prefix_suffixes[suffixes[i]] = "S"

    # Initialize a list to store the result
    result = []

    # Loop through the dictionary and check if the key is a prefix or suffix
    for key in prefix_suffixes:
        if len(key) == n:
            result.append(prefix_suffixes[key])

    # Return the result as a string
    return "".join(result)

