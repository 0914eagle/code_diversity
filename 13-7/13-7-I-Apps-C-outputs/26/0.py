
def get_input():
    N, M = map(int, input().split())
    translators = []
    for _ in range(M):
        translator = list(map(int, input().split()))
        translators.append(translator)
    return N, M, translators

def get_matching(N, M, translators):
    # Initialize a graph with M nodes and 2M edges
    graph = [[] for _ in range(M)]
    for i in range(M):
        for j in range(i+1, M):
            if translators[i][0] == translators[j][1] or translators[i][1] == translators[j][0]:
                graph[i].append(j)
                graph[j].append(i)
    
    # Find a matching using the blossom algorithm
    matching = [0] * M
    for i in range(M):
        if matching[i] == 0:
            visited = [False] * M
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
                        elif matching[neighbor] == 0:
                            matching[node] = neighbor
                            matching[neighbor] = node
                            break
    
    # Check if the matching is complete
    for i in range(M):
        if matching[i] == 0:
            return []
    
    # Return the matching as a list of pairs
    pairs = []
    for i in range(M):
        pairs.append((i, matching[i]))
    return pairs

def main():
    N, M, translators = get_input()
    pairs = get_matching(N, M, translators)
    if pairs:
        for pair in pairs:
            print(pair[0], pair[1])
    else:
        print("impossible")

if __name__ == '__main__':
    main()

