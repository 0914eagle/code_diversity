
def find_matching_code(repository, snippet):
    # Initialize variables
    longest_match = 0
    matching_files = []

    # Iterate through the repository
    for file_name, code in repository.items():
        # Ignore empty lines and lines with only spaces
        code = [line for line in code if line.strip()]
        # Find the longest match in the code
        match = longest_common_substring(code, snippet)
        # If the match is longer than the current longest match, update the variables
        if len(match) > longest_match:
            longest_match = len(match)
            matching_files = [file_name]
        # If the match is the same length as the current longest match, add the file name to the list
        elif len(match) == longest_match:
            matching_files.append(file_name)

    # Return the longest match and the list of matching files
    return longest_match, matching_files

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    result = ""
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > len(result):
                    result = str1[i - dp[i + 1][j + 1] + 1:i + 1]
            else:
                dp[i + 1][j + 1] = 0
    return result

