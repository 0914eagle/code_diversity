
def get_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def is_perfect_matching(R, B, rebels, bases):
    # Initialize a graph with R + B nodes
    graph = [[] for _ in range(R + B)]
    
    # Add edges between rebels and bases
    for i in range(R):
        for j in range(B):
            graph[i].append(B + j)
    
    # Add edges between rebels and bases that are not on the same line
    for i in range(R):
        for j in range(B):
            if rebels[i][0] * bases[j][1] != rebels[i][1] * bases[j][0]:
                graph[i].append(B + j)
    
    # Check if there is a perfect matching in the graph
    visited = [False] * (R + B)
    matching = [False] * R
    for i in range(R):
        if not visited[i]:
            if dfs(graph, visited, matching, i):
                return True
    return False

def dfs(graph, visited, matching, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(graph, visited, matching, neighbor):
                matching[node] = True
                return True
    return False

def main():
    R, B, rebels, bases = get_input()
    if is_perfect_matching(R, B, rebels, bases):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

