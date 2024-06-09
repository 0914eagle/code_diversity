
def solve(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)

    # Initialize a set to store the possible letters for each vertex
    letters = set("abc")

    # Iterate through each vertex and its neighbors
    for vertex in neighbors:
        # If the vertex has no neighbors, it must correspond to the letter "a"
        if not neighbors[vertex]:
            letters.remove("a")
        # If the vertex has one neighbor, it must correspond to the letter "b"
        elif len(neighbors[vertex]) == 1:
            letters.remove("b")
        # If the vertex has two neighbors, it must correspond to the letter "c"
        elif len(neighbors[vertex]) == 2:
            letters.remove("c")
        # If the vertex has more than two neighbors, it is not possible to find a solution
        else:
            return "No"

    # If all letters have been assigned, return "Yes" and the corresponding string
    if not letters:
        return "Yes\n" + "".join(chr(ord('a') + i) for i in range(n))

    # Otherwise, return "No"
    return "No"

