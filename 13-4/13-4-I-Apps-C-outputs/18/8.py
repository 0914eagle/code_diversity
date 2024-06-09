
def longest_match(repository, snippet):
    # Initialize variables
    max_match_length = 0
    matching_files = []

    # Iterate through the repository
    for file_name, file_contents in repository.items():
        # Initialize variables for current file
        current_match_length = 0
        current_match_start = 0

        # Iterate through the snippet
        for i, line in enumerate(snippet):
            # Check if the line is a match
            if line in file_contents[current_match_start:]:
                # Update the current match length and start index
                current_match_length += 1
                current_match_start = file_contents.index(line, current_match_start) + 1
            else:
                # Break if the current match is not a match
                break

        # Check if the current match is the longest match so far
        if current_match_length > max_match_length:
            # Update the max match length and matching files
            max_match_length = current_match_length
            matching_files = [file_name]
        elif current_match_length == max_match_length:
            # Add the file name to the list of matching files
            matching_files.append(file_name)

    # Return the max match length and matching files
    return max_match_length, matching_files

