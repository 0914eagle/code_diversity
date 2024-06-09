
def is_possible(graph, a, b):
    # Initialize the values of the vertices
    values = [0] * len(graph)
    for i in range(len(graph)):
        values[i] = a[i]

    # Iterate through the edges of the graph
    for edge in graph:
        # Get the vertices connected by the edge
        x, y = edge

        # If the value of vertex x is less than the value of vertex y,
        # then decrease the value of vertex x by 1 and increase the value of vertex y by 1
        if values[x] < values[y]:
            values[x] -= 1
            values[y] += 1

        # If the value of vertex x is greater than the value of vertex y,
        # then increase the value of vertex x by 1 and decrease the value of vertex y by 1
        elif values[x] > values[y]:
            values[x] += 1
            values[y] -= 1

        # If the values of vertex x and vertex y are equal,
        # then return False, since it is not possible to achieve the objective
        else:
            return False

    # If all the values of the vertices are equal to the desired values,
    # then return True, since it is possible to achieve the objective
    for i in range(len(graph)):
        if values[i] != b[i]:
            return False
    return True

def main():
    # Read the input from stdin
    num_vertices, num_edges = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    graph = []
    for _ in range(num_edges):
        x, y = map(int, input().split())
        graph.append((x, y))

    # Check if it is possible to achieve the objective
    if is_possible(graph, a, b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

