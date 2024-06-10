
from collections import defaultdict

def build_graph(words):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2)):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                indegree[word2[j]] += 1
                break
    
    return graph, indegree

def topological_sort(graph, indegree):
    result = []
    queue = [char for char in indegree if indegree[char] == 0]
    
    while queue:
        char = queue.pop(0)
        result.append(char)
        
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return ''.join(result) if len(result) == len(indegree) else None

if __name__ == "__main__":
    L, N = input().split()
    N = int(N)
    
    words = [input().strip() for _ in range(N)]
    graph, indegree = build_graph(words)
    result = topological_sort(graph, indegree)
    
    if result is None:
        print("IMPOSSIBLE")
    elif len(result) < len(L):
        print("AMBIGUOUS")
    else:
        print(result)
