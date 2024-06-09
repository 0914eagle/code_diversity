
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Iterate over the prefixes and suffixes and add them to the dictionary
    for prefix in prefixes:
        prefix_suffixes[prefix] = "P"
    for suffix in suffixes:
        prefix_suffixes[suffix] = "S"

    # Initialize an empty list to store the result
    result = []

    # Iterate over the dictionary and add the corresponding character to the result list
    for key in sorted(prefix_suffixes.keys()):
        result.append(prefix_suffixes[key])

    # Return the result list as a string
    return "".join(result)

