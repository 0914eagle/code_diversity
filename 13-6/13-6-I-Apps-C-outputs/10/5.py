
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Count the degree of each vertex
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Find the center of the hedgehog
    center = None
    for i in range(1, n+1):
        if degrees[i] >= 3:
            center = i
            break
    
    # Check if the tree is a k-multihedgehog
    if center is None:
        return "No"
    if k == 1:
        return "Yes"
    else:
        # Find the vertices with degree 1
        vertices = []
        for i in range(1, n+1):
            if degrees[i] == 1:
                vertices.append(i)
        
        # Check if the tree is a (k-1)-multihedgehog
        if len(vertices) == 0:
            return "No"
        else:
            return is_k_multihedgehog(n, k-1, edges+[(center, vertices[0])])

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(is_k_multihedgehog(n, k, edges))

if __name__ == "__main__":
    main()

