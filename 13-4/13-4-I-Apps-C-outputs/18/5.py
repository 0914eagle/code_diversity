
def find_matches(repository, snippet):
    # Initialize variables
    matches = []
    longest_match = 0
    matching_files = []

    # Iterate through the repository
    for file_name, file_contents in repository.items():
        # Iterate through the snippet
        for i in range(len(snippet)):
            # Check if the current line in the snippet is a match for the current line in the file
            if snippet[i] == file_contents[i]:
                # If it is, add it to the matches list
                matches.append(snippet[i])
            # If it's not a match, check if it's a blank line
            elif snippet[i].strip() == "" and file_contents[i].strip() == "":
                # If it is, add it to the matches list
                matches.append(snippet[i])
            # If it's not a match or a blank line, break out of the loop
            else:
                break

        # If the length of the matches list is greater than the longest match found so far, update the longest match and the matching files
        if len(matches) > longest_match:
            longest_match = len(matches)
            matching_files = [file_name]
        # If the length of the matches list is equal to the longest match found so far, add the current file name to the list of matching files
        elif len(matches) == longest_match:
            matching_files.append(file_name)

        # Reset the matches list for the next iteration
        matches = []

    # Return the longest match and the list of matching files
    return longest_match, matching_files

