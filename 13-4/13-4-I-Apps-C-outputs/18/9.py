
def find_matches(repository, snippet):
    # Initialize variables
    matches = []
    longest_match = 0
    matching_files = []

    # Loop through each file in the repository
    for file_name, file_contents in repository.items():
        # Loop through each line in the file
        for i in range(len(file_contents)):
            # Check if the current line matches the first line of the snippet
            if file_contents[i] == snippet[0]:
                # Initialize variables for the current match
                current_match = 1
                current_file = file_name

                # Loop through the remaining lines in the file and the snippet
                for j in range(1, len(file_contents) - i):
                    # Check if the current line in the file matches the current line in the snippet
                    if file_contents[i + j] == snippet[j]:
                        # Increment the current match
                        current_match += 1
                    else:
                        # Break out of the loop if the lines don't match
                        break

                # Check if the current match is the longest match so far
                if current_match > longest_match:
                    # Update the longest match and the matching files
                    longest_match = current_match
                    matching_files = [current_file]
                elif current_match == longest_match:
                    # Add the current file to the list of matching files
                    matching_files.append(current_file)

    # Return the longest match and the list of matching files
    return longest_match, matching_files

