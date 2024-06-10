
def get_conversable_characters(character_list):
    # Initialize a set to store the conversable characters
    conversable_characters = set()

    # Iterate through each character in the list
    for character in character_list:
        # Check if the character is already in the set of conversable characters
        if character not in conversable_characters:
            # If not, add the character to the set and mark it as conversable
            conversable_characters.add(character)
            # Iterate through the list of languages that the character understands
            for language in character.languages:
                # Check if any other character in the list speaks the language
                for other_character in character_list:
                    if language in other_character.languages and other_character != character:
                        # If so, add the other character to the set of conversable characters
                        conversable_characters.add(other_character)
                        # Break out of the inner loop to avoid double-counting
                        break

    # Return the set of conversable characters
    return conversable_characters

def get_non_conversable_characters(character_list, conversable_characters):
    # Initialize a set to store the non-conversable characters
    non_conversable_characters = set()

    # Iterate through each character in the list
    for character in character_list:
        # Check if the character is not in the set of conversable characters
        if character not in conversable_characters:
            # If so, add the character to the set of non-conversable characters
            non_conversable_characters.add(character)

    # Return the set of non-conversable characters
    return non_conversable_characters

def get_smallest_set_of_characters(character_list):
    # Initialize a variable to store the smallest set of characters
    smallest_set = None

    # Iterate through each possible subset of the character list
    for i in range(len(character_list)):
        # Get the subset of characters for this iteration
        subset = get_conversable_characters(character_list[:i+1])
        # If the subset is not empty and (it is the smallest set found so far or there is no smallest set found yet)
        if subset and (not smallest_set or len(subset) < len(smallest_set)):
            # Set the smallest set to this subset
            smallest_set = subset

    # Return the smallest set of characters
    return smallest_set

class Character:
    def __init__(self, name, language, languages):
        self.name = name
        self.language = language
        self.languages = set([language])
        self.languages.update(languages)

    def __repr__(self):
        return f"Character('{self.name}', '{self.language}', {list(self.languages)})"

if __name__ == '__main__':
    # Get the number of characters in the cantina
    num_characters = int(input())

    # Get the information for each character in the cantina
    character_list = []
    for _ in range(num_characters):
        name, language, languages = input().split()
        character_list.append(Character(name, language, languages.split(",")))

    # Get the smallest set of characters that can converse with each other
    smallest_set = get_smallest_set_of_characters(character_list)

    # Print the size of the smallest set of characters
    print(len(smallest_set))

