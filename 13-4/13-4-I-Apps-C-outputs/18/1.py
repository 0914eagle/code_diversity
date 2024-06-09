
def find_matches(repository, snippet):
    # Initialize variables
    matches = []
    longest_match = 0
    matching_files = []

    # Iterate through the repository
    for file_name, file_contents in repository.items():
        # Iterate through the lines of the file
        for i in range(len(file_contents)):
            # Check if the line matches the snippet
            if file_contents[i] == snippet[0]:
                # Initialize the match length and the current match
                match_length = 1
                current_match = [file_contents[i]]

                # Iterate through the remaining lines of the file
                for j in range(i+1, len(file_contents)):
                    # Check if the line matches the next line of the snippet
                    if file_contents[j] == snippet[match_length]:
                        # Add the line to the current match
                        current_match.append(file_contents[j])
                        match_length += 1

                        # Check if the current match is the longest match so far
                        if match_length > longest_match:
                            longest_match = match_length
                            matching_files = [file_name]
                        elif match_length == longest_match:
                            matching_files.append(file_name)

                        # Check if the current match is the entire snippet
                        if match_length == len(snippet):
                            matches.append(current_match)
                            break

    # Return the matches
    return longest_match, matching_files

