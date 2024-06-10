
def is_liked(s):
    # Check if the string contains the substring "one" or "two"
    if "one" in s or "two" in s:
        return False
    return True

def get_removal_indices(s):
    # Initialize variables
    removal_indices = []
    n = len(s)
    
    # Iterate through the string
    for i in range(n-2):
        # Check if the substring s[i:i+3] is "one" or "two"
        if s[i:i+3] in ["one", "two"]:
            # Add the index to the removal indices
            removal_indices.append(i)
    
    # Return the removal indices
    return removal_indices

def get_min_removal_indices(s):
    # Get the removal indices
    removal_indices = get_removal_indices(s)
    
    # Initialize the minimum removal indices
    min_removal_indices = []
    
    # Check if there are any removal indices
    if removal_indices:
        # Sort the removal indices in ascending order
        sorted_removal_indices = sorted(removal_indices)
        
        # Get the first and last indices
        first_index = sorted_removal_indices[0]
        last_index = sorted_removal_indices[-1]
        
        # Check if the first and last indices are consecutive
        if first_index + 1 == last_index:
            # Add the first index to the minimum removal indices
            min_removal_indices.append(first_index)
        else:
            # Add the first and last indices to the minimum removal indices
            min_removal_indices.append(first_index)
            min_removal_indices.append(last_index)
    
    # Return the minimum removal indices
    return min_removal_indices

def main():
    # Read the input
    t = int(input())
    inputs = [input() for _ in range(t)]
    
    # Iterate through the inputs
    for s in inputs:
        # Check if the string is liked
        if is_liked(s):
            # Print 0
            print(0)
        else:
            # Get the minimum removal indices
            min_removal_indices = get_min_removal_indices(s)
            
            # Print the number of removal indices
            print(len(min_removal_indices))
            
            # Print the removal indices
            for i in min_removal_indices:
                print(i, end=" ")
            print()

if __name__ == '__main__':
    main()

