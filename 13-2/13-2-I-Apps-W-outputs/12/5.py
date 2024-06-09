
def get_good_string(strings):
    # Initialize a dictionary to store the frequency of each substring
    substring_freq = {}
    for string in strings:
        # Iterate over the substrings of the current string
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                # Extract the substring and its frequency
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
    
    # Check if all strings are the most frequent substring
    for string in strings:
        if most_frequent_substring not in string:
            return "NO"
    
    # Return the lexicographically minimum good string
    return min(strings)

