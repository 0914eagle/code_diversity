
def get_min_changes(ai_name, phone_name):
    # Initialize a counter for the minimum number of changes
    min_changes = 0
    
    # Iterate through the characters of the AI name
    for i in range(len(ai_name)):
        # Check if the current character is present in the phone name
        if ai_name[i] in phone_name:
            # Increment the minimum number of changes
            min_changes += 1
    
    return min_changes

def get_new_ai_name(ai_name, phone_name, min_changes):
    # Initialize a new string for the new AI name
    new_ai_name = ""
    
    # Iterate through the characters of the AI name
    for i in range(len(ai_name)):
        # Check if the current character is present in the phone name
        if ai_name[i] in phone_name:
            # Add a "#" to the new AI name
            new_ai_name += "#"
        else:
            # Add the current character to the new AI name
            new_ai_name += ai_name[i]
    
    # Return the new AI name
    return new_ai_name

if __name__ == '__main__':
    # Read the input from stdin
    ai_name = input()
    phone_name = input()
    
    # Get the minimum number of changes
    min_changes = get_min_changes(ai_name, phone_name)
    
    # Get the new AI name
    new_ai_name = get_new_ai_name(ai_name, phone_name, min_changes)
    
    # Print the minimum number of changes
    print(min_changes)
    
    # Print the new AI name
    print(new_ai_name)

