
def get_smallest_set_of_characters(characters):
    # Initialize a set to store the characters that can converse with each other
    converse_set = set()

    # Iterate over each character in the input
    for character in characters:
        # Check if the character is already in the converse set
        if character not in converse_set:
            # If not, add the character to the converse set and iterate over the other characters
            converse_set.add(character)
            for other_character in characters:
                # Check if the other character is already in the converse set or if it is the same as the current character
                if other_character not in converse_set and other_character != character:
                    # If not, check if the other character understands the language spoken by the current character
                    if other_character.understands(character.language):
                        # If so, add the other character to the converse set
                        converse_set.add(other_character)

    # Return the size of the converse set
    return len(converse_set)

def main():
    # Read the number of characters from stdin
    num_characters = int(input())

    # Read the characters from stdin
    characters = []
    for _ in range(num_characters):
        name, language, *languages = input().split()
        character = Character(name, language, languages)
        characters.append(character)

    # Call the get_smallest_set_of_characters function and print the result
    print(get_smallest_set_of_characters(characters))

# Define a class to represent a character
class Character:
    def __init__(self, name, language, languages):
        self.name = name
        self.language = language
        self.languages = set(languages)

    def understands(self, language):
        return language in self.languages

# If this program is being run directly (instead of being imported), run the main function
if __name__ == '__main__':
    main()

