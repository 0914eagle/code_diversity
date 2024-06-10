
import itertools

def get_all_non_similar_worlds(n, m):
    # Initialize the graph with only the source and sink vertices
    graph = {0: set(), 1: set()}
    
    # Iterate over the number of changes
    for i in range(n):
        # Add a new vertex and connect it to all existing vertices
        for j in range(2, len(graph)):
            graph[j].add(len(graph))
            graph[len(graph)].add(j)
        
        # Add two edges between the new vertex and the existing vertices
        graph[len(graph)].add(0)
        graph[0].add(len(graph))
        graph[len(graph)].add(1)
        graph[1].add(len(graph))
    
    # Find all non-similar worlds
    non_similar_worlds = set()
    for permutation in itertools.permutations(range(len(graph))):
        world = [set() for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[permutation[i]]:
                world[i].add(permutation[j])
        if len(world[0].intersection(world[1])) >= m:
            non_similar_worlds.add(tuple(frozenset(world[i]) for i in range(len(graph))))
    
    return len(non_similar_worlds)

def get_non_similar_worlds_modulo(n, m):
    return get_all_non_similar_worlds(n, m) % (10**9 + 7)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_non_similar_worlds_modulo(n, m))

