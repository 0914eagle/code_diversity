
def is_good_graph(n, m, edges):
    # Initialize a set to store the vertices that are connected to vertex 1
    connected_to_1 = set()
    # Initialize a set to store the vertices that are connected to vertex n
    connected_to_n = set()
    # Iterate over the edges
    for i in range(m):
        # Get the vertices of the current edge
        u, v = edges[i]
        # If vertex 1 is connected to vertex v, add vertex v to the set of connected vertices
        if u == 1:
            connected_to_1.add(v)
        # If vertex n is connected to vertex u, add vertex u to the set of connected vertices
        if v == n:
            connected_to_n.add(u)
    # Return True if vertex 1 is not connected to vertex n and there are no self-loops or multi-edges, False otherwise
    return len(connected_to_1) == 0 and len(connected_to_n) == 0

def play_game(n, m, edges):
    # Initialize the winner to None
    winner = None
    # Initialize the number of moves to 0
    num_moves = 0
    # While the game is not over
    while winner is None:
        # If it is Taro's turn
        if num_moves % 2 == 0:
            # If the graph is not good, set the winner to Jiro
            if not is_good_graph(n, m, edges):
                winner = "Jiro"
            # Otherwise, add an edge connecting vertex 1 and vertex n
            else:
                edges.append((1, n))
                m += 1
        # If it is Jiro's turn
        else:
            # If the graph is not good, set the winner to Taro
            if not is_good_graph(n, m, edges):
                winner = "Taro"
            # Otherwise, add an edge connecting two arbitrary vertices
            else:
                edges.append((random.randint(1, n), random.randint(1, n)))
                m += 1
        # Increment the number of moves
        num_moves += 1
    # Return the winner
    return winner

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())
    # Iterate over the test cases
    for _ in range(t):
        # Read the number of vertices and edges
        n, m = map(int, input().split())
        # Read the edges
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        # Play the game and get the winner
        winner = play_game(n, m, edges)
        # Print the winner
        print(winner)

