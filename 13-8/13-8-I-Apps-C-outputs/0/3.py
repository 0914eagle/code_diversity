
def get_longest_match(repository, snippet):
    longest_match = 0
    matching_files = []
    for file_name, file_content in repository.items():
        match_count = 0
        for line1, line2 in zip(file_content.splitlines(), snippet.splitlines()):
            if line1.strip() == line2.strip():
                match_count += 1
        if match_count > longest_match:
            longest_match = match_count
            matching_files = [file_name]
        elif match_count == longest_match:
            matching_files.append(file_name)
    return longest_match, matching_files

