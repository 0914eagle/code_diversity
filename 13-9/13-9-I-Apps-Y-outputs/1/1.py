
def get_characters_to_leave(characters):
    # Initialize a set to store the characters to leave
    characters_to_leave = set()

    # Iterate over each character and their languages
    for character, languages in characters.items():
        # Check if the character can converse with anyone else in the cantina
        can_converse = False
        for other_character, other_languages in characters.items():
            # Skip if the other character is the same as the current character
            if other_character == character:
                continue

            # Check if the other character's languages include the current character's language
            if languages[0] in other_languages:
                can_converse = True
                break

        # If the character cannot converse with anyone else, add them to the set of characters to leave
        if not can_converse:
            characters_to_leave.add(character)

    # Return the size of the set of characters to leave
    return len(characters_to_leave)

def main():
    # Read the number of characters and their languages from stdin
    num_characters = int(input())
    characters = {}
    for _ in range(num_characters):
        character, language, *other_languages = input().split()
        characters[character] = [language] + other_languages

    # Call the get_characters_to_leave function and print the result
    print(get_characters_to_leave(characters))

if __name__ == '__main__':
    main()

