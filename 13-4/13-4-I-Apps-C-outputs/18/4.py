
def get_matching_fragments(repository, snippet):
    # Initialize variables
    matches = []
    longest_match = 0
    matching_files = []

    # Iterate through the repository fragments
    for file_name, fragment in repository.items():
        # Initialize variables for this fragment
        current_match = 0
        current_files = []

        # Iterate through the lines of the fragment and the snippet
        for i in range(len(fragment)):
            # Check if the lines match
            if fragment[i] == snippet[i]:
                current_match += 1
                current_files.append(file_name)
            else:
                # If the lines don't match, check if this is a longer match than the previous one
                if current_match > longest_match:
                    longest_match = current_match
                    matching_files = current_files
                break

        # If the fragment is a match, add it to the list of matches
        if current_match == len(fragment):
            matches.append((current_match, current_files))

    # Return the longest match and the list of matching files
    return longest_match, matching_files

