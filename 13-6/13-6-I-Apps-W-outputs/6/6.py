
def get_jump_ability(string):
    # Initialize variables
    jump_ability = 0
    vowels = set("AEIOUY")
    current_pos = 0

    # Iterate through the string
    for i, char in enumerate(string):
        # If the current character is a vowel, update the jump ability
        if char in vowels:
            jump_ability = max(jump_ability, i - current_pos + 1)
            current_pos = i + 1

    # Return the minimum jump ability needed to reach the end of the string
    return jump_ability

def main():
    string = input("Enter a string: ")
    print(get_jump_ability(string))

if __name__ == '__main__':
    main()

