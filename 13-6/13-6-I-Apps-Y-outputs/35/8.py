
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffix_dict = {}

    # Iterate over the prefixes and suffixes
    for prefix in prefixes:
        for suffix in suffixes:
            # If the prefix and suffix are not the same string
            if prefix != suffix:
                # Check if the prefix is a prefix of the suffix
                if suffix.startswith(prefix):
                    # If it is, add it to the dictionary with the key as the prefix and the value as the suffix
                    prefix_suffix_dict[prefix] = suffix

    # Initialize a list to store the results
    results = []

    # Iterate over the prefixes and suffixes
    for prefix in prefixes:
        # Check if the prefix is a key in the dictionary
        if prefix in prefix_suffix_dict:
            # If it is, add 'P' to the results list
            results.append('P')
        else:
            # If it's not, add 'S' to the results list
            results.append('S')

    # Join the results list into a string and return it
    return ''.join(results)

