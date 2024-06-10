
def is_leaf(graph, vertex):
    # Check if the vertex is a leaf vertex (connected to only one edge)
    return len(graph[vertex]) == 1


def can_move(graph, vertex, destination):
    # Check if the pig can move from the current vertex to the destination vertex
    return destination in graph[vertex] and destination not in graph.keys()


def remove_wolves(graph, pigs):
    # Initialize the minimum number of wolves to remove as 0
    min_wolves = 0
    # Initialize a set to keep track of the pigs that have escaped
    escaped_pigs = set()
    # Iterate through the pigs
    for pig in pigs:
        # If the pig is on a leaf vertex, it can escape
        if is_leaf(graph, pig):
            escaped_pigs.add(pig)
        # Otherwise, check if the pig can move to any of its neighboring vertices
        else:
            for neighbor in graph[pig]:
                # If the pig can move to a neighboring vertex and the neighbor is not occupied by a wolf, the pig can escape
                if can_move(graph, pig, neighbor) and neighbor not in graph.keys():
                    escaped_pigs.add(pig)
                    break
    # If not all pigs have escaped, increase the minimum number of wolves to remove by 1
    if len(escaped_pigs) < len(pigs):
        min_wolves += 1
    return min_wolves


def main():
    # Read the input
    v, p = map(int, input().split())
    graph = {}
    for _ in range(v - 1):
        u, v = map(int, input().split())
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    pigs = list(map(int, input().split()))
    # Call the remove_wolves function and print the result
    print(remove_wolves(graph, pigs))


if __name__ == '__main__':
    main()

