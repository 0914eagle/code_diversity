
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that can converse with each other
    converse_set = set()

    # Iterate over each character in the input
    for character in characters:
        # Check if the character is already in the converse set
        if character in converse_set:
            continue

        # Iterate over each other character in the input
        for other_character in characters:
            # Check if the other character is already in the converse set
            if other_character in converse_set:
                continue

            # Check if the character and other character can converse with each other
            if can_converse(character, other_character):
                # Add the character and other character to the converse set
                converse_set.add(character)
                converse_set.add(other_character)
                break

    # Return the size of the converse set
    return len(converse_set)

def can_converse(character1, character2):
    # Check if the characters speak the same language
    if character1["language"] == character2["language"]:
        return True

    # Check if one character understands the other character's language
    if character1["language"] in character2["understands"] or character2["language"] in character1["understands"]:
        return True

    # Check if there is a sequence of intermediate languages that can be used for translation
    for language in character1["understands"]:
        if language in character2["understands"]:
            return True

    # If none of the above conditions are met, the characters cannot converse
    return False

def main():
    # Read the input
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        character = input().split()
        characters.append({
            "name": character[0],
            "language": character[1],
            "understands": character[2:]
        })

    # Call the function to get the smallest set of characters that can converse with each other
    smallest_set_size = get_smallest_set_of_characters(characters)

    # Print the output
    print(smallest_set_size)

if __name__ == "__main__":
    main()

