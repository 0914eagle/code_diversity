
def count_good_substrings(s, k):
    # Initialize a dictionary to store the count of good substrings
    good_substrings = {}

    # Iterate over the characters of the input string
    for i in range(len(s)):
        # Check if the current character is good
        if s[i].isalpha() and s[i].islower():
            # If the current character is good, check if the substring starting from the current character and ending at the previous good character is good
            if i > 0 and s[i-1].isalpha() and s[i-1].islower():
                substring = s[i-1:i+1]
                if substring not in good_substrings or good_substrings[substring] <= k:
                    good_substrings[substring] = good_substrings.get(substring, 0) + 1

    # Return the number of distinct good substrings
    return len(good_substrings)

