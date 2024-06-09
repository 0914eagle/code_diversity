
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degrees of each vertex
    degrees = {i: 0 for i in range(1, n + 1)}

    # Count the degrees of each vertex
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    # Find the center of the hedgehog
    center = None
    for vertex, degree in degrees.items():
        if degree >= 3:
            center = vertex
            break

    # Check if the tree is a k-multihedgehog
    if k == 1:
        # For k=1, the tree should be a hedgehog with one center and n-1 vertices of degree 1
        return degrees[center] == 3 and all(degree == 1 for degree in degrees.values())
    else:
        # For k>1, the tree should be a (k-1)-multihedgehog with one center and n-1 vertices of degree 1
        return is_k_multihedgehog(n, k - 1, edges) and degrees[center] == 3 and all(degree == 1 for degree in degrees.values())

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("Yes") if is_k_multihedgehog(n, k, edges) else print("No")

if __name__ == "__main__":
    main()

