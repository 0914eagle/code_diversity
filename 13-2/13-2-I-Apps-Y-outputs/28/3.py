
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that can converse with each other
    converse_set = set()

    # Iterate over each character in the input
    for character in characters:
        # Check if the character is already in the converse set
        if character in converse_set:
            continue

        # Get the languages spoken and understood by the character
        spoken_languages = set(character["spoken_languages"])
        understood_languages = set(character["understood_languages"])

        # Get the characters that can converse with the current character
        converse_with = get_converse_characters(characters, spoken_languages, understood_languages)

        # Add the current character and the characters that can converse with it to the converse set
        converse_set.add(character)
        converse_set.update(converse_with)

    # Return the size of the smallest set of characters that can converse with each other
    return len(converse_set)

def get_converse_characters(characters, spoken_languages, understood_languages):
    # Initialize a set to store the characters that can converse with the current character
    converse_with = set()

    # Iterate over each character in the input
    for character in characters:
        # Check if the character is already in the converse set or the current character
        if character in converse_with or character == spoken_languages:
            continue

        # Get the languages spoken and understood by the character
        character_spoken_languages = set(character["spoken_languages"])
        character_understood_languages = set(character["understood_languages"])

        # Check if the current character can converse with the character
        if len(spoken_languages.intersection(character_understood_languages)) > 0 and len(understood_languages.intersection(character_spoken_languages)) > 0:
            converse_with.add(character)

    # Return the set of characters that can converse with the current character
    return converse_with

def main():
    # Read the input
    num_characters = int(input())
    characters = []
    for _ in range(num_characters):
        character = input().split()
        spoken_languages = set(character[1].split(","))
        understood_languages = set(character[2:])
        characters.append({"name": character[0], "spoken_languages": spoken_languages, "understood_languages": understood_languages})

    # Get the smallest set of characters that can converse with each other
    smallest_set_size = get_smallest_set_of_characters(characters)

    # Print the size of the smallest set of characters
    print(smallest_set_size)

if __name__ == '__main__':
    main()

