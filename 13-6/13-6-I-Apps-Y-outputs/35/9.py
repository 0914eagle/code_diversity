
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Loop through the prefixes and suffixes and add them to the dictionary
    for prefix in prefixes:
        prefix_suffixes[prefix] = "P"
    for suffix in suffixes:
        prefix_suffixes[suffix] = "S"

    # Initialize an empty string to store the result
    result = ""

    # Loop through the dictionary and append the corresponding value to the result string
    for i in range(1, n):
        result += prefix_suffixes[prefixes[i-1]]

    return result

