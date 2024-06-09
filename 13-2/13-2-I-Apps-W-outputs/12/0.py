
def get_good_string(strings):
    # Initialize a dictionary to store the frequency of each substring
    substring_freq = {}
    for string in strings:
        # Iterate over the substrings of the current string
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                # Get the substring and its frequency
                substring = string[i:j]
                freq = substring_freq.get(substring, 0) + 1
                substring_freq[substring] = freq
    
    # Find the most frequent substring
    most_frequent_substring = ""
    most_frequent_freq = 0
    for substring, freq in substring_freq.items():
        if freq > most_frequent_freq:
            most_frequent_substring = substring
            most_frequent_freq = freq
    
    # Find all strings that contain the most frequent substring
    good_strings = []
    for string in strings:
        if most_frequent_substring in string:
            good_strings.append(string)
    
    # If there are no good strings, return "NO"
    if not good_strings:
        return "NO"
    
    # Otherwise, return the lexicographically minimum good string
    return min(good_strings)

