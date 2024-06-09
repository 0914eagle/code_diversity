
def get_disagreeing_pairs(N, K, disagreements):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the disagreements
    for i in range(N):
        for j in range(i+1, N):
            if i in disagreements[j] or j in disagreements[i]:
                graph[i].append(j)
                graph[j].append(i)

    # Return the maximum size of a clique in the graph
    return max(map(len, cliques(graph)))

def cliques(graph):
    for i in range(len(graph)):
        for c in cliques_rec(graph, i, []):
            yield c

def cliques_rec(graph, i, clique):
    if i == len(graph):
        yield clique
    else:
        for j in range(len(graph[i])):
            if graph[i][j] not in clique:
                for c in cliques_rec(graph, i+1, clique + [graph[i][j]]):
                    yield c

def main():
    N, K = map(int, input().split())
    disagreements = [set(map(int, input().split())) for _ in range(N)]
    print(get_disagreeing_pairs(N, K, disagreements))

if __name__ == '__main__':
    main()

