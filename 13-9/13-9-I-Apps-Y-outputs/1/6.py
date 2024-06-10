
def get_characters_to_leave(characters):
    # Initialize a set to store the characters to leave
    characters_to_leave = set()

    # Iterate over each character in the input
    for character in characters:
        # Check if the character is able to converse with anyone else in the cantina
        if not can_converse_with_anyone(character, characters):
            # If not, add the character to the set of characters to leave
            characters_to_leave.add(character)

    # Return the size of the set of characters to leave
    return len(characters_to_leave)

def can_converse_with_anyone(character, characters):
    # Iterate over each other character in the cantina
    for other_character in characters:
        # Check if the other character is able to converse with the current character
        if can_converse_with(character, other_character):
            # If so, return True
            return True

    # If no other character is able to converse with the current character, return False
    return False

def can_converse_with(character1, character2):
    # Get the languages spoken by both characters
    languages1 = set(character1.languages)
    languages2 = set(character2.languages)

    # Check if there is at least one language that both characters speak
    if len(languages1.intersection(languages2)) > 0:
        # If so, return True
        return True

    # If no language is common to both characters, return False
    return False

class Character:
    def __init__(self, name, language, languages):
        self.name = name
        self.language = language
        self.languages = set([language])
        self.languages.update(languages)

if __name__ == '__main__':
    # Read the number of characters in the cantina
    n = int(input())

    # Read the information for each character
    characters = []
    for _ in range(n):
        name, language, languages = input().split()
        characters.append(Character(name, language, languages.split(',')))

    # Get the size of the smallest set of characters to leave
    characters_to_leave = get_characters_to_leave(characters)

    # Print the size of the smallest set of characters to leave
    print(characters_to_leave)

