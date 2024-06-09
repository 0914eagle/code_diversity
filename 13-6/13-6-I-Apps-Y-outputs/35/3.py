
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Loop through the prefixes and suffixes and add them to the dictionary
    for prefix in prefixes:
        prefix_suffixes[prefix] = "P"
    for suffix in suffixes:
        prefix_suffixes[suffix] = "S"

    # Initialize a list to store the result
    result = []

    # Loop through the dictionary and add the prefixes and suffixes to the result list
    for key in sorted(prefix_suffixes):
        result.append(prefix_suffixes[key])

    # Return the result list
    return "".join(result)

