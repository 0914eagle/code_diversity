
def solve_problem(n, m, k, edges):
    # Initialize a set to store the vertices in the independent set
    independent_set = set()
    # Initialize a set to store the vertices in the cycle
    cycle = set()
    # Initialize a variable to store the length of the cycle
    cycle_length = 0

    # Iterate over the edges
    for edge in edges:
        # If the edge connects two vertices that are already in the independent set, remove one of them from the independent set
        if edge[0] in independent_set and edge[1] in independent_set:
            independent_set.remove(edge[0] if edge[0] != edge[1] else edge[1])
        # If the edge connects two vertices that are already in the cycle, add the third vertex to the cycle
        elif edge[0] in cycle and edge[1] in cycle:
            cycle.add(edge[2])
        # If the edge connects a vertex in the independent set and a vertex not in the independent set, add the vertex to the independent set
        elif edge[0] in independent_set and edge[1] not in independent_set:
            independent_set.add(edge[1])
        # If the edge connects a vertex not in the independent set and a vertex in the independent set, add the vertex to the independent set
        elif edge[0] not in independent_set and edge[1] in independent_set:
            independent_set.add(edge[0])
        # If the edge connects two vertices not in the independent set, add the first vertex to the independent set and the second vertex to the cycle
        else:
            independent_set.add(edge[0])
            cycle.add(edge[1])
            cycle_length += 1

    # If the length of the cycle is at most k, return the cycle
    if cycle_length <= k:
        return [2, cycle_length] + list(cycle)
    # Otherwise, return the independent set
    else:
        return [1, len(independent_set)] + list(independent_set)

