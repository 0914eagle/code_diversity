
def is_sortable(s, k):
    
    # Initialize a list to store the indices of the letters in their original order
    original_indices = list(range(len(s)))
    # Loop through each letter in the string
    for i in range(len(s)):
        # Find the index of the letter in its original order
        original_index = original_indices.index(i)
        # Check if the letter is in its correct position
        if s[i] != chr(ord('a') + original_index):
            # Find the index of the letter in its current position
            current_index = s.index(s[i])
            # Check if the letter can be swapped with the letter in its correct position
            if abs(current_index - original_index) >= k:
                # Swap the letters
                s = s[:current_index] + s[original_index] + s[current_index + 1:original_index] + s[original_index + 1] + s[current_index + 1:]
                # Update the list of original indices
                original_indices[current_index] = original_indices[original_index]
                original_indices[original_index] = current_index
    # Check if all letters are in their correct position
    return all(s[i] == chr(ord('a') + i) for i in range(len(s)))

