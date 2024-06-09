
def get_smallest_set_of_characters(characters):
    # Initialize a graph with an edge between two characters if they can converse
    graph = {}
    for character in characters:
        graph[character] = []
        for other_character in characters:
            if character != other_character and can_converse(character, other_character):
                graph[character].append(other_character)

    # Find the smallest set of characters that can converse with each other
    visited = set()
    to_visit = [characters[0]]
    while to_visit:
        character = to_visit.pop()
        if character not in visited:
            visited.add(character)
            to_visit += graph[character]

    return len(visited)

def can_converse(character1, character2):
    # Check if the two characters speak the same language
    if character1[1] == character2[1]:
        return True

    # Check if one character understands the other's language
    for language in character1[2:]:
        if language == character2[1]:
            return True
    for language in character2[2:]:
        if language == character1[1]:
            return True

    return False

def main():
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        name, language = input().split()
        languages = [language]
        for j in range(20):
            language = input()
            if language:
                languages.append(language)
        characters.append((name, language, *languages))
    print(get_smallest_set_of_characters(characters))

if __name__ == '__main__':
    main()

