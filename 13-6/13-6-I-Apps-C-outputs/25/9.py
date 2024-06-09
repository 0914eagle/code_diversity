
def is_good_graph(graph):
    # Check if graph is good
    for i in range(1, len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i] in graph[j]:
                return False
    return True

def add_edge(graph, a, b):
    # Add edge between a and b
    graph[a].append(b)
    graph[b].append(a)
    return graph

def play_game(graph):
    # Play game optimally
    while is_good_graph(graph):
        # Taro's turn
        a, b = 1, 2
        graph = add_edge(graph, a, b)
        if not is_good_graph(graph):
            return "First"
        # Jiro's turn
        a, b = 1, 3
        graph = add_edge(graph, a, b)
        if not is_good_graph(graph):
            return "Second"
    return "First"

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            a, b = map(int, input().split())
            graph = add_edge(graph, a, b)
        print(play_game(graph))

