
def solve(repository, snippet):
    # Initialize a dictionary to store the file names and their contents
    file_names = {}
    for file_name, content in repository:
        file_names[file_name] = content

    # Initialize a list to store the longest match and the file names of the matching fragments
    longest_match = []
    matching_file_names = []

    # Iterate through the lines of the snippet
    for line in snippet:
        # Ignore empty lines and lines with only spaces
        if not line.strip():
            continue

        # Iterate through the file names and their contents in the repository
        for file_name, content in file_names.items():
            # Find the longest match between the current line and the content of the file
            match = longest_common_subsequence(line, content)

            # If the match is longer than the current longest match, update the longest match and the file names of the matching fragments
            if len(match) > len(longest_match):
                longest_match = match
                matching_file_names = [file_name]

            # If the match is equal to the current longest match, add the file name to the list of matching file names
            elif len(match) == len(longest_match):
                matching_file_names.append(file_name)

    # Return the length of the longest match and the file names of the matching fragments
    return len(longest_match), " ".join(matching_file_names)

# Function to find the longest common subsequence between two strings
def longest_common_subsequence(str1, str2):
    # Find the length of the strings
    m = len(str1)
    n = len(str2)

    # Initialize a 2D array to store the longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the first row and first column of the array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the length of the longest common subsequence
    result = dp[m][n]

    # Return the longest common subsequence
    return str1[:result]

