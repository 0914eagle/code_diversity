
def get_min_replacements(ai_name, phone_name):
    # Initialize a counter for the minimum number of replacements
    min_replacements = 0
    
    # Iterate through the characters of the AI name
    for i in range(len(ai_name)):
        # If the current character is in the phone name, increment the counter
        if ai_name[i] in phone_name:
            min_replacements += 1
    
    # Return the minimum number of replacements
    return min_replacements

def get_new_ai_name(ai_name, phone_name, min_replacements):
    # Initialize an empty string for the new AI name
    new_ai_name = ""
    
    # Iterate through the characters of the AI name
    for i in range(len(ai_name)):
        # If the current character is not in the phone name, add it to the new AI name
        if ai_name[i] not in phone_name:
            new_ai_name += ai_name[i]
        # Otherwise, if the minimum number of replacements has not been reached, add a "#" character to the new AI name
        elif min_replacements > 0:
            new_ai_name += "#"
            min_replacements -= 1
    
    # Return the new AI name
    return new_ai_name

if __name__ == '__main__':
    ai_name = input("Enter the name of the AI: ")
    phone_name = input("Enter the name of the phone: ")
    min_replacements = get_min_replacements(ai_name, phone_name)
    new_ai_name = get_new_ai_name(ai_name, phone_name, min_replacements)
    print(f"The minimum number of replacements is {min_replacements}.")
    print(f"The new name of the AI is {new_ai_name}.")

