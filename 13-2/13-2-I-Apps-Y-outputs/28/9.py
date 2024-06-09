
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that can converse with each other
    converse_set = set()

    # Iterate over the characters
    for character in characters:
        # Check if the character is already in the converse set
        if character in converse_set:
            continue

        # Get the languages spoken and understood by the character
        spoken_languages = set(character["spoken_languages"])
        understood_languages = set(character["understood_languages"])

        # Get the characters that can converse with the current character
        converse_with = [c for c in characters if c != character and c["spoken_languages"] & spoken_languages and c["understood_languages"] & understood_languages]

        # Add the current character and the characters that can converse with it to the converse set
        converse_set.add(character)
        converse_set.update(converse_with)

    # Return the size of the converse set
    return len(converse_set)

def main():
    # Read the number of characters
    num_characters = int(input())

    # Read the characters
    characters = []
    for _ in range(num_characters):
        # Read the character name, spoken languages, and understood languages
        character_name, spoken_languages, understood_languages = input().split()

        # Create a dictionary for the character
        character = {
            "name": character_name,
            "spoken_languages": spoken_languages.split(","),
            "understood_languages": understood_languages.split(","),
        }

        # Add the character to the list of characters
        characters.append(character)

    # Get the size of the smallest set of characters that can converse with each other
    smallest_set_size = get_smallest_set_of_characters(characters)

    # Print the size of the smallest set
    print(smallest_set_size)

if __name__ == "__main__":
    main()

