
def is_good_graph(n, m, edges):
    # Initialize a set to store the edges
    edge_set = set()
    
    # Loop through the given edges
    for edge in edges:
        # If the edge is not a self-loop and is not already in the set, add it to the set
        if edge[0] != edge[1] and edge not in edge_set:
            edge_set.add(edge)
    
    # If the set size is equal to the number of edges, return True
    if len(edge_set) == m:
        return True
    else:
        return False

def get_winner(n, m, edges):
    # Initialize variables to store the winner and the current graph
    winner = ""
    current_graph = edges
    
    # Loop through the edges
    for i in range(m):
        # If the current graph is not a good graph, break the loop
        if not is_good_graph(n, m, current_graph):
            break
        
        # If it is Taro's turn, add an edge connecting vertices 1 and 2 to the current graph
        if i % 2 == 0:
            current_graph.append([1, 2])
        
        # If it is Jiro's turn, add an edge connecting vertices 1 and N to the current graph
        else:
            current_graph.append([1, n])
    
    # If the current graph is a good graph, Taro wins
    if is_good_graph(n, m, current_graph):
        winner = "First"
    
    # If the current graph is not a good graph, Jiro wins
    else:
        winner = "Second"
    
    # Return the winner
    return winner

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        edges = []
        
        for _ in range(m):
            a, b = map(int, input().split())
            edges.append([a, b])
        
        print(get_winner(n, m, edges))

