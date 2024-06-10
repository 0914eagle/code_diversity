
from collections import defaultdict

def create_graph(words):
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
    queue = [char for char in indegree if indegree[char] == 0]
    result = []
    
    while queue:
        char = queue.pop(0)
        result.append(char)
        
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(indegree) else None

def find_alphabet_order(L, words):
    graph, indegree = create_graph(words)
    order = topological_sort(graph, indegree)
    
    if order is None:
        return "IMPOSSIBLE"
    elif len(order) < len(L):
        return "AMBIGUOUS"
    else:
        return "".join(order)

if __name__ == "__main__":
    L, N = input().split()
    N = int(N)
    words = [input().strip() for _ in range(N)]
    
    result = find_alphabet_order(L, words)
    print(result)
