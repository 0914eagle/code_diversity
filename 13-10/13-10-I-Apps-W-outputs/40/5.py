
def get_dominos_on_edges(graph):
    n = len(graph)
    m = len(graph[0])
    dominos = []
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == 1:
                dominos.append([i, j])
    return dominos

def main():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    dominos = get_dominos_on_edges(graph)
    print(len(dominos))

if __name__ == '__main__':
    main()

