
def get_liked_string(s):
    # Check if the string contains "one" or "two" as a substring
    if "one" in s or "two" in s:
        return "Disliked"
    
    # Check if the string contains two consecutive characters that are the same
    if len(s) > 1 and s[0] == s[1]:
        return "Disliked"
    
    # If the string is liked, return the original string
    return s

def get_removed_indices(s):
    # Initialize variables
    removed_indices = []
    index = 0
    
    # Loop through the string and check if the current character is the same as the previous character
    while index < len(s) - 1:
        if s[index] == s[index + 1]:
            # If the current character is the same as the previous character, add the index to the removed indices list
            removed_indices.append(index)
        index += 1
    
    # Return the removed indices list
    return removed_indices

def get_minimum_removed_indices(s):
    # Get the liked string
    liked_string = get_liked_string(s)
    
    # If the string is disliked, return 0
    if liked_string == "Disliked":
        return 0
    
    # Get the removed indices
    removed_indices = get_removed_indices(s)
    
    # Return the minimum number of removed indices needed to make the string liked
    return len(removed_indices)

def get_removed_indices_list(s):
    # Get the liked string
    liked_string = get_liked_string(s)
    
    # If the string is disliked, return an empty list
    if liked_string == "Disliked":
        return []
    
    # Get the removed indices
    removed_indices = get_removed_indices(s)
    
    # Return the removed indices list
    return removed_indices

if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        s = input()
        print(get_minimum_removed_indices(s))
        print(" ".join(str(i) for i in get_removed_indices_list(s)))

