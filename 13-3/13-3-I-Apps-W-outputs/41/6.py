
def is_sortable(s, k):
    # Initialize a list to store the sorted string
    sorted_string = list(s)
    # Loop through each letter in the string
    for i in range(len(s)):
        # Find the index of the letter that is closest to the current letter but greater than it
        closest_greater_index = -1
        for j in range(i+1, len(s)):
            if abs(i-j) >= k and sorted_string[j] > sorted_string[i]:
                closest_greater_index = j
                break
        # If there is no letter greater than the current letter, return "No"
        if closest_greater_index == -1:
            return "No"
        # Swap the current letter with the closest greater letter
        sorted_string[i], sorted_string[closest_greater_index] = sorted_string[closest_greater_index], sorted_string[i]
    # If all letters are sorted, return "Yes"
    return "Yes"

