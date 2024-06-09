
def get_maximum_score(n, m, edges):
    # Initialize the score and the current vertex
    score = 0
    current_vertex = 1

    # Loop through each edge
    for edge in edges:
        # If the current vertex is the starting vertex of the edge
        if current_vertex == edge[0]:
            # Move the piece to the ending vertex of the edge and add the weight to the score
            current_vertex = edge[1]
            score += edge[2]

    # Return the maximum possible score
    return score

def main():
    # Read the input data
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    # Find the maximum possible score
    score = get_maximum_score(n, m, edges)

    # Print the result
    print(score)

if __name__ == '__main__':
    main()

