
def find_matches(repository, code_snippet):
    # Initialize a dictionary to store the matches
    matches = {}

    # Iterate over the repository fragments
    for fragment in repository:
        # Initialize a counter for the number of consecutive matching lines
        count = 0

        # Iterate over the lines of the fragment and the code snippet
        for i in range(len(fragment)):
            # Check if the line is not empty or contains only spaces
            if fragment[i].strip() and code_snippet[i].strip():
                # Check if the line is a match
                if fragment[i].strip() == code_snippet[i].strip():
                    # Increment the counter
                    count += 1
                # If the line is not a match, break the loop
                else:
                    break

        # If at least one line matched, add the fragment to the matches dictionary
        if count > 0:
            matches[count] = matches.get(count, []) + [fragment]

    # Return the matches dictionary
    return matches

