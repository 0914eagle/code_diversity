
def f1(n, p, x):
    # f1(n, p, x) takes three inputs:
    # n is the number of vertices in the tree
    # p is a list of the parent of each vertex (p[i] is the parent of vertex i)
    # x is a list of the favorite integer sequence of Snuke (x[i] is the favorite integer of vertex i)
    
    # Initialize the color and weight of each vertex to be white and 0, respectively
    color = ["white"] * (n + 1)
    weight = [0] * (n + 1)
    
    # Set the color and weight of the root vertex (vertex 1) to be black and x[1], respectively
    color[1] = "black"
    weight[1] = x[1]
    
    # Iterate through each vertex in the tree (except the root vertex)
    for i in range(2, n + 1):
        # If the parent of the current vertex is black, set the color of the current vertex to be black and its weight to be x[i]
        if color[p[i]] == "black":
            color[i] = "black"
            weight[i] = x[i]
        # If the parent of the current vertex is white, set the color of the current vertex to be white and its weight to be x[i] - x[p[i]]
        else:
            color[i] = "white"
            weight[i] = x[i] - x[p[i]]
    
    # Check if the weight of each vertex is non-negative
    for i in range(1, n + 1):
        if weight[i] < 0:
            return "IMPOSSIBLE"
    
    # If all weights are non-negative, return "POSSIBLE"
    return "POSSIBLE"

def f2(n, p, x):
    # f2(n, p, x) takes three inputs:
    # n is the number of vertices in the tree
    # p is a list of the parent of each vertex (p[i] is the parent of vertex i)
    # x is a list of the favorite integer sequence of Snuke (x[i] is the favorite integer of vertex i)
    
    # Initialize the color and weight of each vertex to be white and 0, respectively
    color = ["white"] * (n + 1)
    weight = [0] * (n + 1)
    
    # Set the color and weight of the root vertex (vertex 1) to be black and x[1], respectively
    color[1] = "black"
    weight[1] = x[1]
    
    # Iterate through each vertex in the tree (except the root vertex)
    for i in range(2, n + 1):
        # If the parent of the current vertex is black, set the color of the current vertex to be black and its weight to be x[i]
        if color[p[i]] == "black":
            color[i] = "black"
            weight[i] = x[i]
        # If the parent of the current vertex is white, set the color of the current vertex to be white and its weight to be x[i] - x[p[i]]
        else:
            color[i] = "white"
            weight[i] = x[i] - x[p[i]]
    
    # Check if the weight of each vertex is non-negative
    for i in range(1, n + 1):
        if weight[i] < 0:
            return "IMPOSSIBLE"
    
    # If all weights are non-negative, return "POSSIBLE"
    return "POSSIBLE"

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print(f1(n, p, x))
    print(f2(n, p, x))

