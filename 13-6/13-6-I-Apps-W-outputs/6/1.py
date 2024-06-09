
def get_min_jump_ability(string):
    # Initialize variables
    jump_ability = 1
    current_position = 0
    vowels = ["A", "E", "I", "O", "U", "Y"]

    # Iterate through the string
    for i in range(len(string)):
        # If the current character is a vowel, update the current position
        if string[i] in vowels:
            current_position += 1
        # If the current position is greater than the jump ability, update the jump ability
        if current_position > jump_ability:
            jump_ability = current_position

    return jump_ability

def main():
    string = input("Enter a string: ")
    print(get_min_jump_ability(string))

if __name__ == "__main__":
    main()

