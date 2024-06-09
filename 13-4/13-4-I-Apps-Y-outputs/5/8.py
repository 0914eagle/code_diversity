
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that need to leave
    characters_to_leave = set()

    # Iterate over each character in the input
    for character in characters:
        # Check if the character is able to converse with anyone else in the input
        can_converse = False
        for other_character in characters:
            if character != other_character and can_converse_with(character, other_character):
                can_converse = True
                break

        # If the character cannot converse with anyone else, add it to the set of characters to leave
        if not can_converse:
            characters_to_leave.add(character)

    # Return the size of the smallest set of characters that need to leave
    return len(characters_to_leave)

# Check if two characters can converse with each other
def can_converse_with(character1, character2):
    # Get the languages spoken by both characters
    languages1 = set(character1[1:])
    languages2 = set(character2[1:])

    # Check if there is at least one language that both characters speak
    if len(languages1.intersection(languages2)) > 0:
        return True
    else:
        return False

