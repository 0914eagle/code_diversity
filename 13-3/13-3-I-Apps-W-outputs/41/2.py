
def is_sorted(s, k):
    # Initialize a list to store the sorted string
    sorted_string = list(s)

    # Loop through each letter in the string
    for i in range(len(s)):
        # Find the index of the letter that is greater than the current letter
        # and is at a distance of at least k from the current letter
        greater_index = None
        for j in range(i + 1, len(s)):
            if s[j] > s[i] and abs(j - i) >= k:
                greater_index = j
                break

        # If a greater letter is found, swap it with the current letter
        if greater_index is not None:
            sorted_string[i], sorted_string[greater_index] = sorted_string[greater_index], sorted_string[i]

    # Check if the sorted string is sorted in increasing order
    return "".join(sorted_string) == sorted(s)

