
def solve(s, k):
    # Initialize a dictionary to store the number of good substrings
    # for each prefix of the string
    prefix_counts = {}
    prefix_counts[""] = 1

    # Iterate through the string and calculate the number of good substrings
    # for each prefix
    for i in range(len(s)):
        # Get the current prefix
        prefix = s[:i+1]

        # If the prefix is already in the dictionary, it means we have already
        # calculated the number of good substrings for this prefix, so we can skip it
        if prefix in prefix_counts:
            continue

        # Get the number of good substrings for the previous prefix
        prev_prefix_count = prefix_counts.get(prefix[:-1], 0)

        # If the last character of the prefix is good, add the number of good
        # substrings for the previous prefix to the current prefix
        if s[i] == "1":
            prefix_counts[prefix] = prev_prefix_count + 1
        # If the last character of the prefix is bad, add the number of good
        # substrings for the previous prefix to the current prefix, but make sure
        # to subtract the number of bad characters that are already in the prefix
        else:
            prefix_counts[prefix] = prev_prefix_count - min(k, prefix.count("0"))

    # Return the number of good substrings for the entire string
    return prefix_counts[s]

