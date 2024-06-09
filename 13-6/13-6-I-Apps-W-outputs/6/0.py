
def get_jump_ability(string):
    # Initialize variables
    jump_ability = 0
    vowels = ["A", "E", "I", "O", "U", "Y"]
    
    # Iterate through the string
    for i in range(len(string)):
        # If the current character is a vowel, increase the jump ability
        if string[i] in vowels:
            jump_ability += 1
        # If the current character is not a vowel and the jump ability is not zero, return the current jump ability
        elif jump_ability != 0:
            return jump_ability
    
    # If the string is empty or all characters are consonants, return 0
    return 0

def main():
    string = input("Enter a string: ")
    print(get_jump_ability(string))

if __name__ == "__main__":
    main()

