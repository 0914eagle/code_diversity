
def solve(s, t):
    # Initialize a dictionary to store the count of each letter in t
    letter_count = {}
    for letter in t:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    # Initialize a variable to store the maximum number of occurrences
    max_occurrences = 0

    # Iterate through the string s and check if each letter is in t
    for i in range(len(s)):
        if s[i] in letter_count:
            # If the letter is in t, decrement the count for that letter
            letter_count[s[i]] -= 1
            if letter_count[s[i]] == 0:
                # If the count is 0, it means we have found a match for all letters in t
                max_occurrences += 1

    return max_occurrences
