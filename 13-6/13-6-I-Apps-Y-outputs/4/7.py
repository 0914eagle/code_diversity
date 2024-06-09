
def solve(s, k):
    n = len(s)
    # Initialize a dictionary to store the frequency of each character
    freq = {"R": 0, "G": 0, "B": 0}
    for c in s:
        freq[c] += 1
    # Initialize the minimum number of changes required
    min_changes = n
    # Iterate over the frequency of each character
    for c in freq:
        # If the frequency of the current character is greater than the length of the substring, we can remove that character and still have a substring of length k
        if freq[c] > k:
            min_changes = min(min_changes, freq[c] - k)
    return min_changes

