
def get_smallest_conversable_set(characters):
    # Create a graph with the characters as nodes and edges between characters that can converse
    graph = {}
    for character in characters:
        graph[character] = []
        for other_character in characters:
            if character != other_character and can_converse(character, other_character):
                graph[character].append(other_character)

    # Find the smallest subset of characters that covers all nodes in the graph
    return len(get_minimum_spanning_tree(graph))

def can_converse(character1, character2):
    # Check if the two characters can converse by checking if they speak the same language or if there is a third character that can translate between them
    return character1.language == character2.language or any(can_converse(character1, third_character) and can_converse(third_character, character2) for third_character in characters)

def get_minimum_spanning_tree(graph):
    # Find the smallest subset of characters that covers all nodes in the graph
    visited = set()
    minimum_spanning_tree = []
    for character in graph:
        if character not in visited:
            minimum_spanning_tree.append(character)
            visited.add(character)
            for other_character in graph[character]:
                if other_character not in visited:
                    minimum_spanning_tree.append(other_character)
                    visited.add(other_character)
    return minimum_spanning_tree

class Character:
    def __init__(self, name, language, understood_languages):
        self.name = name
        self.language = language
        self.understood_languages = understood_languages

    def __eq__(self, other):
        return self.name == other.name and self.language == other.language and self.understood_languages == other.understood_languages

if __name__ == '__main__':
    num_characters = int(input())
    characters = []
    for _ in range(num_characters):
        name, language, *understood_languages = input().split()
        characters.append(Character(name, language, understood_languages))
    print(get_smallest_conversable_set(characters))

