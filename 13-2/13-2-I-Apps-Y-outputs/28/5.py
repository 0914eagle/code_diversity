
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that can converse with each other
    converse_set = set()

    # Iterate over each character and its languages
    for character, languages in characters.items():
        # Check if the character can converse with any other character in the set
        can_converse = False
        for other_character in converse_set:
            if other_character in languages:
                can_converse = True
                break

        # If the character cannot converse with any other character, add it to the set
        if not can_converse:
            converse_set.add(character)

    # Return the size of the smallest set of characters that can converse with each other
    return len(converse_set)

def main():
    # Read the number of characters and their languages from stdin
    num_characters = int(input())
    characters = {}
    for _ in range(num_characters):
        character, language, *languages = input().split()
        characters[character] = set([language] + languages)

    # Call the function to get the smallest set of characters that can converse with each other
    smallest_set_size = get_smallest_set_of_characters(characters)

    # Print the size of the smallest set
    print(smallest_set_size)

if __name__ == '__main__':
    main()

