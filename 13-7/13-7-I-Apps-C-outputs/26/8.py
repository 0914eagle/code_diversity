
def get_matching(num_languages, num_translators, translators):
    # Initialize a graph with translators as nodes and languages as edges
    graph = {}
    for i in range(num_translators):
        graph[i] = set()
    for translator, languages in translators:
        for language in languages:
            graph[translator].add(language)

    # Find a maximum matching in the graph
    matching = []
    visited = set()
    while graph:
        # Pick an unvisited node (translator) and explore its neighbors
        node = next(iter(graph))
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                matching.append((node, neighbor))
                visited.add(neighbor)
                graph.pop(neighbor)
                break
        graph.pop(node)

    # Check if the matching is complete
    if len(matching) == num_translators / 2:
        return matching
    else:
        return "impossible"

def main():
    num_languages, num_translators = map(int, input().split())
    translators = []
    for _ in range(num_translators):
        translator, languages = map(int, input().split())
        translators.append((translator, set(map(int, input().split()))))
    print(get_matching(num_languages, num_translators, translators))

if __name__ == '__main__':
    main()

