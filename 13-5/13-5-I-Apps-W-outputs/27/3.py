
def solve(n, m, k, edges):
    # Initialize a set to store the vertices in the independent set
    independent_set = set()
    # Initialize a list to store the vertices in the cycle
    cycle = []
    # Iterate through the edges
    for edge in edges:
        # If the edge connects two vertices that are already in the independent set, remove the smaller vertex from the independent set
        if edge[0] in independent_set and edge[1] in independent_set:
            if edge[0] < edge[1]:
                independent_set.remove(edge[0])
            else:
                independent_set.remove(edge[1])
        # If the edge connects a vertex in the independent set to a vertex not in the independent set, add the vertex to the independent set
        elif edge[0] in independent_set and edge[1] not in independent_set:
            independent_set.add(edge[1])
        elif edge[0] not in independent_set and edge[1] in independent_set:
            independent_set.add(edge[0])
        # If the edge connects two vertices not in the independent set, add the smaller vertex to the independent set and add the larger vertex to the cycle
        else:
            if edge[0] < edge[1]:
                independent_set.add(edge[0])
                cycle.append(edge[1])
            else:
                independent_set.add(edge[1])
                cycle.append(edge[0])
    # If the size of the independent set is greater than or equal to the ceiling of k/2, return the independent set
    if len(independent_set) >= k//2+1:
        return 1, list(independent_set)
    # If the size of the cycle is less than or equal to k, return the cycle
    elif len(cycle) <= k:
        return 2, cycle
    # Otherwise, return -1 to indicate that neither problem can be solved
    else:
        return -1, []

