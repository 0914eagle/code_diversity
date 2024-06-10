
def get_min_replacements(ai_name, phone_name):
    # Initialize a counter for the minimum number of replacements
    min_replacements = 0
    # Loop through the characters of the AI name
    for i in range(len(ai_name)):
        # If the current character is in the phone name, increment the counter
        if ai_name[i] in phone_name:
            min_replacements += 1
    # Return the minimum number of replacements
    return min_replacements

def get_new_ai_name(ai_name, phone_name, min_replacements):
    # Initialize a list to store the new AI name
    new_ai_name = []
    # Loop through the characters of the AI name
    for i in range(len(ai_name)):
        # If the current character is in the phone name, add a "#" to the new AI name
        if ai_name[i] in phone_name:
            new_ai_name.append("#")
        # Otherwise, add the current character to the new AI name
        else:
            new_ai_name.append(ai_name[i])
    # Join the characters of the new AI name into a string and return it
    return "".join(new_ai_name)

if __name__ == '__main__':
    ai_name = input("Enter the name of the AI: ")
    phone_name = input("Enter the name of the phone: ")
    min_replacements = get_min_replacements(ai_name, phone_name)
    new_ai_name = get_new_ai_name(ai_name, phone_name, min_replacements)
    print(f"The minimum number of replacements is {min_replacements}.")
    print(f"The new name of the AI is {new_ai_name}.")

