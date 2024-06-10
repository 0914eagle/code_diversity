
import sys

def get_independent_set(graph):
    independent_set = []
    for vertex in range(len(graph)):
        if vertex not in independent_set:
            for neighbor in graph[vertex]:
                if neighbor in independent_set:
                    break
            else:
                independent_set.append(vertex)
    return len(independent_set)

def main():
    num_vertices, num_edges = map(int, input().split())
    graph = [[] for _ in range(num_vertices + 1)]
    for _ in range(num_edges):
        vertex1, vertex2 = map(int, input().split())
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    print(get_independent_set(graph))

if __name__ == '__main__':
    main()

