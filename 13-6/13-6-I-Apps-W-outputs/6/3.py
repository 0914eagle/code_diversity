
def get_jump_ability(string):
    # Initialize variables
    jump_ability = 0
    vowels = ["A", "E", "I", "O", "U", "Y"]
    
    # Iterate through the string
    for i in range(len(string)):
        # If the current character is a vowel, increment the jump ability
        if string[i] in vowels:
            jump_ability += 1
        # If the current character is not a vowel and the jump ability is greater than 0, break the loop
        elif jump_ability > 0:
            break
    
    return jump_ability

def main():
    string = input("Enter a string: ")
    print(get_jump_ability(string))

if __name__ == "__main__":
    main()

