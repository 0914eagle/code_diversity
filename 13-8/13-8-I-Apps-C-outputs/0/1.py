
def longest_match(repository, snippet):
    # Initialize the longest match length and file names
    longest_length = 0
    file_names = []
    
    # Iterate over the repository fragments
    for file_name, fragment in repository:
        # Initialize the current match length
        current_length = 0
        
        # Iterate over the lines of the fragment and the snippet
        for frag_line, snip_line in zip(fragment, snippet):
            # Ignore empty lines and lines with only spaces
            if frag_line.strip() and snip_line.strip():
                # Check if the lines match
                if frag_line.strip() == snip_line.strip():
                    current_length += 1
                else:
                    break
        
        # Check if the current match length is longer than the longest match length
        if current_length > longest_length:
            # Update the longest match length and file names
            longest_length = current_length
            file_names = [file_name]
        # Check if the current match length is equal to the longest match length
        elif current_length == longest_length:
            # Add the file name to the list of file names
            file_names.append(file_name)
    
    # Return the longest match length and file names
    return longest_length, file_names

