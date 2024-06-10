
def get_liked_string(s):
    # Initialize variables
    liked = True
    indices_to_remove = []
    
    # Check if the string contains "one" or "two"
    if "one" in s or "two" in s:
        liked = False
    
    # Check if the string contains "oneone" or "twotwo"
    for i in range(len(s) - 2):
        if s[i:i+3] == "one" or s[i:i+3] == "two":
            liked = False
            indices_to_remove.append(i)
    
    # Return the liked string and the indices to remove
    return liked, indices_to_remove

def get_min_indices(s):
    # Initialize variables
    liked, indices_to_remove = get_liked_string(s)
    min_indices = []
    
    # If the string is not liked, find the minimum number of indices to remove
    if not liked:
        # Sort the indices in ascending order
        indices_to_remove.sort()
        # Find the minimum number of indices to remove
        min_indices = [indices_to_remove[0]]
        for i in range(1, len(indices_to_remove)):
            if indices_to_remove[i] != indices_to_remove[i-1] + 1:
                min_indices.append(indices_to_remove[i])
        # Return the minimum number of indices and the indices themselves
        return len(min_indices), min_indices
    else:
        # If the string is liked, return 0 and an empty list
        return 0, []

def main():
    # Read the input
    t = int(input())
    strings = []
    for i in range(t):
        strings.append(input())
    
    # Call the function to get the minimum number of indices
    for s in strings:
        num_indices, indices = get_min_indices(s)
        print(num_indices)
        if num_indices > 0:
            print(" ".join(map(str, indices)))
        else:
            print()

if __name__ == '__main__':
    main()

