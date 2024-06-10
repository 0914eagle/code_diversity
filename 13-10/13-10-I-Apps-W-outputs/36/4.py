
def get_liked_string(s):
    # Initialize variables
    liked = True
    remove_indices = []

    # Check if the string contains "one" or "two" as a substring
    if "one" in s or "two" in s:
        liked = False

    # Check if the string contains "oneone" or "two" as a substring
    if "oneone" in s or "two" in s:
        liked = False

    # Check if the string contains "one" or "two" as a substring
    if "one" in s or "two" in s:
        liked = False

    # If the string is liked, return an empty list of remove indices
    if liked:
        return remove_indices

    # If the string is not liked, return a list of all indices to remove
    else:
        return list(range(len(s)))

def get_minimum_remove_indices(s):
    # Initialize variables
    remove_indices = get_liked_string(s)
    minimum_remove_indices = []

    # If there are no indices to remove, return an empty list
    if not remove_indices:
        return minimum_remove_indices

    # If there are indices to remove, return the minimum number of indices needed to make the string liked
    else:
        return [min(remove_indices)]

if __name__ == '__main__':
    s = "onetwone"
    print(get_liked_string(s))
    print(get_minimum_remove_indices(s))

