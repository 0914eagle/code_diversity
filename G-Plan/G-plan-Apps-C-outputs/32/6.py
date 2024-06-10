
from collections import defaultdict

def build_graph(words):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2)):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                in_degree[word2[j]] += 1
                break
    
    return graph, in_degree

def topological_sort(graph, in_degree):
    queue = [char for char in in_degree if in_degree[char] == 0]
    result = ''
    
    while queue:
        char = queue.pop(0)
        result += char
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(in_degree) else None

if __name__ == "__main__":
    L, N = input().split()
    N = int(N)
    
    words = [input().strip() for _ in range(N)]
    
    graph, in_degree = build_graph(words)
    result = topological_sort(graph, in_degree)
    
    if result is None:
        print("IMPOSSIBLE")
    elif len(result) < len(in_degree):
        print("AMBIGUOUS")
    else:
        print(result)
