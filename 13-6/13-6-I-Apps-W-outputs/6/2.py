
def find_min_jump_ability(string):
    # Initialize variables
    jump_ability = 0
    current_position = 0
    vowels = ["A", "E", "I", "O", "U", "Y"]

    # Iterate through the string
    for i in range(len(string)):
        # If the current character is a vowel, increase the jump ability
        if string[i] in vowels:
            jump_ability += 1
        # If the current character is not a vowel, decrease the jump ability
        else:
            jump_ability -= 1
        # If the jump ability becomes negative, return -1 (impossible to reach the end of the string)
        if jump_ability < 0:
            return -1
        # If the current position is the last character of the string, return the jump ability
        if i == len(string) - 1:
            return jump_ability

def main():
    string = input("Enter a string: ")
    print(find_min_jump_ability(string))

if __name__ == '__main__':
    main()

