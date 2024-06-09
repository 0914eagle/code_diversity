
def get_smallest_set_of_characters(characters):
    # Initialize a graph with an edge between each pair of characters that can converse
    graph = {}
    for character in characters:
        graph[character] = []
        for other_character in characters:
            if character != other_character and can_converse(character, other_character):
                graph[character].append(other_character)

    # Find the smallest set of characters that cover all the edges in the graph
    visited = set()
    smallest_set = []
    for character in characters:
        if character not in visited:
            dfs(graph, character, visited, smallest_set)

    return len(smallest_set)

def can_converse(character1, character2):
    # Check if either character speaks the other's language
    return character1["language"] == character2["language"] or character1["language"] in character2["understands"] or character2["language"] in character1["understands"]

def dfs(graph, character, visited, smallest_set):
    if character not in visited:
        visited.add(character)
        smallest_set.append(character)
        for neighbor in graph[character]:
            dfs(graph, neighbor, visited, smallest_set)

if __name__ == '__main__':
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        name, language, *understands = input().split()
        characters.append({"name": name, "language": language, "understands": understands})
    print(get_smallest_set_of_characters(characters))

