
def get_good_string(strings):
    # Step 1: Initialize a dictionary to store the frequency of each substring
    substring_freq = {}
    for string in strings:
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                if substring not in substring_freq:
                    substring_freq[substring] = 1
                else:
                    substring_freq[substring] += 1
    
    # Step 2: Find the most frequent substring
    most_frequent_substring = ""
    most_frequent_substring_freq = 0
    for substring, freq in substring_freq.items():
        if freq > most_frequent_substring_freq:
            most_frequent_substring = substring
            most_frequent_substring_freq = freq
    
    # Step 3: Check if all strings are the most frequent substring
    for string in strings:
        if most_frequent_substring not in string:
            return "NO"
    
    # Step 4: Return the lexicographically minimum good string
    good_strings = []
    for string in strings:
        if most_frequent_substring in string:
            good_strings.append(string)
    good_strings.sort()
    return good_strings[0]

