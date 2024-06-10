
def get_domino_placements(n, m, edges):
    # Initialize a dictionary to store the number of domino placements for each vertex
    domino_placements = {i: 0 for i in range(1, n + 1)}

    # Iterate over the edges and update the domino placements for each vertex
    for edge in edges:
        vertex1, vertex2 = edge
        domino_placements[vertex1] += 1
        domino_placements[vertex2] += 1

    # Return the maximum number of domino placements
    return max(domino_placements.values())

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(get_domino_placements(n, m, edges))

if __name__ == '__main__':
    main()

