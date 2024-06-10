
from collections import defaultdict

def build_graph(words):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        j = 0
        while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
            j += 1
        if j < len(word1) and j < len(word2):
            graph[word1[j]].append(word2[j])
            in_degree[word2[j]] += 1

    return graph, in_degree

def topological_sort(graph, in_degree):
    result = []
    queue = [char for char in in_degree if in_degree[char] == 0]

    while queue:
        char = queue.pop(0)
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(result) if len(result) == len(in_degree) else None

if __name__ == "__main__":
    L, N = input().split()
    N = int(N)
    words = [input().strip() for _ in range(N)]

    graph, in_degree = build_graph(words)
    result = topological_sort(graph, in_degree)

    if result:
        print(result)
    else:
        print("IMPOSSIBLE" if len(graph) > 0 else "AMBIGUOUS")
