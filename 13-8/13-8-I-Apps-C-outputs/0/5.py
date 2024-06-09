
def longest_match(repository, snippet):
    # Initialize variables
    matches = []
    longest_match_length = 0
    longest_match_files = []

    # Iterate through each file in the repository
    for file in repository:
        # Initialize variables for current file
        current_match_length = 0
        current_match_files = []

        # Iterate through each line in the file
        for line in file:
            # Check if the line is a match
            if line in snippet:
                # Increment the match length
                current_match_length += 1
                # Add the file to the list of matching files
                current_match_files.append(file)

        # Check if the current match length is the longest match length
        if current_match_length > longest_match_length:
            # Update the longest match length and files
            longest_match_length = current_match_length
            longest_match_files = current_match_files

    # Return the longest match length and files
    return longest_match_length, longest_match_files

