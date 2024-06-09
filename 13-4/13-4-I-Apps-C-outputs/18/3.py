
def find_matching_fragments(repository, snippet):
    # Initialize a dictionary to store the fragments and their file names
    fragments = {}

    # Iterate through the repository and add each fragment to the dictionary
    for file_name, fragment in repository:
        fragments[fragment] = file_name

    # Initialize a variable to store the longest match
    longest_match = 0

    # Iterate through the snippet and check for matches in the dictionary
    for line in snippet:
        for fragment in fragments:
            # Check if the line is a match for the fragment
            if line == fragment:
                # If it is, update the longest match and add the file name to the list
                longest_match = max(longest_match, len(fragment))
                file_names.append(fragments[fragment])

    # Return the longest match and the list of file names
    return longest_match, file_names

