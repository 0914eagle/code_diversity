
def get_min_replacements(ai_name, phone_name):
    # Initialize variables
    replacements = 0
    i = 0
    j = 0

    # Loop through the AI name and compare it to the phone name
    while i < len(ai_name) and j < len(phone_name):
        if ai_name[i] == phone_name[j]:
            replacements += 1
            i += 1
            j += 1
        else:
            i += 1

    # Return the minimum number of replacements needed
    return replacements

def main():
    # Read the input
    ai_name = input()
    phone_name = input()

    # Call the get_min_replacements function and print the result
    print(get_min_replacements(ai_name, phone_name))

if __name__ == '__main__':
    main()

