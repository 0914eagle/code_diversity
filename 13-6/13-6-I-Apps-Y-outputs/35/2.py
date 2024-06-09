
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Iterate over the prefixes and suffixes
    for prefix in prefixes:
        for suffix in suffixes:
            # If the prefix is a suffix, add it to the dictionary with the value "P"
            if prefix == suffix:
                prefix_suffixes[prefix] = "P"
            # If the suffix is a prefix, add it to the dictionary with the value "S"
            elif suffix in prefix:
                prefix_suffixes[suffix] = "S"

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the prefixes and suffixes
    for prefix in prefixes:
        # If the prefix is in the dictionary, add its value to the result string
        if prefix in prefix_suffixes:
            result += prefix_suffixes[prefix]
        # If the prefix is not in the dictionary, add "P" to the result string
        else:
            result += "P"

    # Return the result string
    return result

