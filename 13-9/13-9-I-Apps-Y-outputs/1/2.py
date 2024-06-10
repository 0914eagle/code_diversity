
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that can converse with each other
    converse_set = set()

    # Iterate over the characters
    for character in characters:
        # Check if the character is able to converse with anyone in the set
        can_converse = False
        for other_character in converse_set:
            if can_converse_with(character, other_character):
                can_converse = True
                break

        # If the character can converse with anyone in the set, add it to the set
        if can_converse:
            converse_set.add(character)

    # Return the size of the smallest set of characters that can converse with each other
    return len(converse_set)

def can_converse_with(character1, character2):
    # Check if the characters speak the same language
    if character1["language"] == character2["language"]:
        return True

    # Check if one of the characters understands the other's language
    for language in character1["understands"]:
        if language in character2["understands"]:
            return True

    # If neither of the characters speak the same language and no one understands the other's language, they cannot converse
    return False

def parse_input(input_string):
    # Split the input string into a list of characters
    characters = input_string.split()

    # Create a dictionary for each character with their name, language, and languages they understand
    character_info = []
    for character in characters:
        character_dict = {}
        character_dict["name"] = character.split("-")[0]
        character_dict["language"] = character.split("-")[1]
        character_dict["understands"] = character.split("-")[2:]
        character_info.append(character_dict)

    return character_info

def main():
    # Read the input from stdin
    input_string = input()

    # Parse the input into a list of characters
    characters = parse_input(input_string)

    # Get the size of the smallest set of characters that can converse with each other
    smallest_set_size = get_smallest_set_of_characters(characters)

    # Print the size of the smallest set
    print(smallest_set_size)

if __name__ == '__main__':
    main()

