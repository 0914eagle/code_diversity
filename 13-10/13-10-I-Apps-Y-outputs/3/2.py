
def simplify_string(string):
    # Convert the string to a set to remove duplicates
    simplified_string = set(string)
    # Return the length of the simplified string
    return len(simplified_string)

def min_erase_for_simplify(string):
    # Get the simplicity of the string
    simplicity = simplify_string(string)
    # If the simplicity is 1 or 2, return 0
    if simplicity <= 2:
        return 0
    # Otherwise, return the number of letters to erase to simplify the string
    return len(string) - simplicity + 2

if __name__ == '__main__':
    string = input()
    print(min_erase_for_simplify(string))

