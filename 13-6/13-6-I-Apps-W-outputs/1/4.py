
def solve(n, x, edges):
    # Create a graph object
    graph = {}
    for edge in edges:
        graph[edge[0]] = edge[1]
    
    # Initialize the number of moves for Alice and Bob
    alice_moves = 0
    bob_moves = 0
    
    # Initialize the current position for Alice and Bob
    alice_pos = 1
    bob_pos = x
    
    # While Alice and Bob are not at the same position
    while alice_pos != bob_pos:
        # Alice moves
        alice_moves += 1
        alice_pos = graph[alice_pos]
        
        # Bob moves
        bob_moves += 1
        bob_pos = graph[bob_pos]
    
    # Return the total number of moves
    return alice_moves + bob_moves

