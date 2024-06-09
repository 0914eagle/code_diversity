
def find_matches(repository, snippet):
    # Initialize a dictionary to store the matches
    matches = {}

    # Iterate over the fragments in the repository
    for file_name, fragment in repository.items():
        # Initialize a counter to store the longest match length
        longest_match_length = 0

        # Iterate over the lines of the fragment
        for i in range(len(fragment)):
            # Check if the line matches the snippet
            if fragment[i] == snippet[i]:
                # Increment the longest match length
                longest_match_length += 1
            else:
                # Break the loop if the line does not match
                break

        # Add the match to the dictionary
        matches[file_name] = longest_match_length

    # Return the matches
    return matches

