
def get_cycle_length(graph):
    for node in graph:
        if node in graph[node]:
            return len(graph[node])
    return -1

def build_graph(n, a):
    graph = {}
    for i in range(n):
        graph[i] = set()
        for j in range(i+1, n):
            if a[i] & a[j] != 0:
                graph[i].add(j)
                graph[j].add(i)
    return graph

def main():
    n = int(input())
    a = list(map(int, input().split()))
    graph = build_graph(n, a)
    print(get_cycle_length(graph))

if __name__ == '__main__':
    main()

