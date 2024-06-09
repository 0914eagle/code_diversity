
def f1(n):
    # Calculate the number of independent sets in the graph
    num_independent_sets = (1 << n) - 1
    return num_independent_sets

def f2(n, edges):
    # Initialize the answer and the number of vertices in the graph
    answer = 0
    num_vertices = n
    
    # Iterate over all edges in the graph
    for edge in edges:
        # Find the vertices connected by the edge
        u, v = edge[0], edge[1]
        
        # If the edge is not a tree edge, update the answer and the number of vertices in the graph
        if u != v:
            answer += num_vertices - 2
            num_vertices -= 1
    
    return answer

if __name__ == '__main__':
    n = int(input())
    edges = []
    
    # Read the input edges
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Calculate the sum of the number of independent sets in all edge-induced subgraphs
    answer = f1(n)
    for edge in edges:
        answer += f2(n, [edge])
    
    # Output the answer modulo 998,244,353
    print(answer % 998244353)

