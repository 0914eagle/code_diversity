
def solve(s, t):
    # Initialize a dictionary to store the count of each letter in t
    letter_count = {}
    for letter in t:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1

    # Initialize the maximum number of occurrences to 0
    max_occurrences = 0

    # Iterate through the string s and check if the letter at each index is in the dictionary
    for i in range(len(s)):
        if s[i] in letter_count:
            # If the letter is in the dictionary, decrement the count for that letter
            letter_count[s[i]] -= 1
            if letter_count[s[i]] == 0:
                # If the count is 0, it means we have found a match for one of the letters in t
                max_occurrences += 1

    return max_occurrences

