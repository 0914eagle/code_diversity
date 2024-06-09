
def solve(n, prefixes, suffixes):
    # Initialize a dictionary to store the prefixes and suffixes
    prefix_suffixes = {}

    # Loop through the prefixes and suffixes and add them to the dictionary
    for prefix in prefixes:
        prefix_suffixes[prefix] = "P"
    for suffix in suffixes:
        prefix_suffixes[suffix] = "S"

    # Initialize a list to store the answers
    answers = []

    # Loop through the dictionary and check if the key is a prefix or suffix
    for key in prefix_suffixes:
        if key in prefixes:
            answers.append("P")
        else:
            answers.append("S")

    # Return the answers as a string
    return "".join(answers)

