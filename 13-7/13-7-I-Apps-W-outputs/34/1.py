
def is_perfect_matching_possible(rebels, bases):
    # Initialize a graph with rebels as nodes and bases as edges
    graph = {}
    for rebel in rebels:
        graph[rebel] = set()
    for base in bases:
        graph[base] = set()
    
    # Add edges between rebels and bases
    for rebel in rebels:
        for base in bases:
            if rebel != base:
                graph[rebel].add(base)
    
    # Check if there is a perfect matching in the graph
    matching = []
    for rebel in rebels:
        if len(graph[rebel]) == 1:
            matching.append((rebel, graph[rebel].pop()))
    
    # Check if all rebels have been matched
    if len(matching) == len(rebels):
        return True
    else:
        return False

def main():
    rebels, bases = map(int, input().split())
    rebels = [(int(x), int(y)) for x, y in [input().split() for _ in range(rebels)]]
    bases = [(int(x), int(y)) for x, y in [input().split() for _ in range(bases)]]
    print("Yes") if is_perfect_matching_possible(rebels, bases) else print("No")

if __name__ == '__main__':
    main()

