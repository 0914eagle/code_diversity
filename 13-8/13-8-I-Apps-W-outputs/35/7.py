
def get_min_replacements(ai_name, phone_name):
    # Initialize a variable to keep track of the minimum number of replacements
    min_replacements = float('inf')
    
    # Loop through all possible positions of the phone name in the AI name
    for i in range(len(ai_name) - len(phone_name) + 1):
        # Check if the phone name is a substring of the AI name at the current position
        if ai_name[i:i+len(phone_name)] == phone_name:
            # If it is, calculate the number of replacements needed to remove the phone name
            replacements = len(phone_name)
            
            # Update the minimum number of replacements if necessary
            if replacements < min_replacements:
                min_replacements = replacements
    
    # Return the minimum number of replacements
    return min_replacements

def main():
    # Read the input
    ai_name = input()
    phone_name = input()
    
    # Call the get_min_replacements function and print the result
    print(get_min_replacements(ai_name, phone_name))

if __name__ == '__main__':
    main()

