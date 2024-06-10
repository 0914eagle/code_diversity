
from collections import defaultdict

def build_graph(words):
    graph = defaultdict(list)
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2)):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                break
    return graph

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = [node for node in in_degree if in_degree[node] == 0]
    result = ""
    while queue:
        node = queue.pop(0)
        result += node
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else "IMPOSSIBLE"

if __name__ == "__main__":
    L, N = input().split()
    N = int(N)
    words = [input().strip() for _ in range(N)]
    graph = build_graph(words)
    result = topological_sort(graph)
    print(result if len(result) > 0 else "AMBIGUOUS")
