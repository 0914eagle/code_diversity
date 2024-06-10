
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
    
    return result if len(result) == len(in_degree) else 'IMPOSSIBLE'

def find_alphabet_order(L, N, words):
    graph, in_degree = build_graph(words)
    alphabet_order = topological_sort(graph, in_degree)
    
    if alphabet_order == 'IMPOSSIBLE':
        return alphabet_order
    elif len(alphabet_order) < len(L):
        return 'AMBIGUOUS'
    else:
        return alphabet_order

if __name__ == "__main__":
    L, N = input().split()
    words = [input().strip() for _ in range(int(N))]
    result = find_alphabet_order(L, N, words)
    print(result)
