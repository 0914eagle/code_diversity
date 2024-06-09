
def find_matches(repository, snippet):
    # Initialize variables
    matches = []
    longest_match = 0
    matching_files = []

    # Iterate through the repository
    for file_name, code in repository.items():
        # Initialize variables for current file
        current_match = 0
        current_files = []

        # Iterate through the code lines
        for i, line in enumerate(code.splitlines()):
            # Check if the line is empty or contains only spaces
            if not line.strip():
                continue

            # Check if the line matches the snippet
            if line.strip() == snippet.splitlines()[i].strip():
                current_match += 1
                current_files.append(file_name)

        # Add the current match to the matches list
        matches.append((current_match, current_files))

        # Update the longest match if necessary
        if current_match > longest_match:
            longest_match = current_match
            matching_files = current_files

    # Return the longest match and the matching files
    return longest_match, matching_files

