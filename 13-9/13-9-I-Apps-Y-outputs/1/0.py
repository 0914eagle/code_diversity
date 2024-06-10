
def get_characters_to_leave(characters):
    # Initialize a set to store the characters to leave
    characters_to_leave = set()

    # Iterate over each character in the input list
    for character in characters:
        # Check if the current character is already in the set of characters to leave
        if character in characters_to_leave:
            continue

        # Get the languages spoken by the current character
        languages = set(character["languages"])

        # Iterate over each other character in the input list
        for other_character in characters:
            # Check if the current character and other character are the same
            if character == other_character:
                continue

            # Check if the other character is already in the set of characters to leave
            if other_character in characters_to_leave:
                continue

            # Get the languages spoken by the other character
            other_languages = set(other_character["languages"])

            # Check if the current character and other character can converse
            if len(languages.intersection(other_languages)) == 0:
                # If not, add the other character to the set of characters to leave
                characters_to_leave.add(other_character)

    # Return the size of the set of characters to leave
    return len(characters_to_leave)

def main():
    # Read the number of characters and their languages from stdin
    num_characters = int(input())
    characters = []
    for _ in range(num_characters):
        character_info = input().split()
        character = {
            "name": character_info[0],
            "languages": character_info[1:]
        }
        characters.append(character)

    # Get the size of the smallest set of characters to leave
    characters_to_leave = get_characters_to_leave(characters)

    # Print the size of the smallest set of characters to leave
    print(characters_to_leave)

if __name__ == '__main__':
    main()

