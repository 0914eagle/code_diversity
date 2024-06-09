
def longest_match(repository, snippet):
    # Initialize variables
    matches = []
    longest_match_length = 0
    longest_match_files = []

    # Iterate through the repository
    for file_name, code in repository.items():
        # Initialize variables for current file
        current_match_length = 0
        current_match_files = []

        # Iterate through the code in the current file
        for i, line in enumerate(code):
            # Check if the line matches the snippet
            if line.strip() == snippet[i].strip():
                current_match_length += 1
                current_match_files.append(file_name)
            else:
                # If the line doesn't match, check if it's a longer match
                if current_match_length > longest_match_length:
                    longest_match_length = current_match_length
                    longest_match_files = current_match_files
                break

        # If the current file has a longer match, update the variables
        if current_match_length > longest_match_length:
            longest_match_length = current_match_length
            longest_match_files = current_match_files

    # Return the longest match length and files
    return longest_match_length, longest_match_files

