
import sys
input = sys.stdin.read()
input = input.split('\n')

n, m, s = map(int, input[0].split())

edges = []
for i in range(1, m+1):
    t, u, v = map(int, input[i].split())
    edges.append((t, u, v))

def max_plan():
    # Initialize the plan with the starting vertex
    plan = [s]
    undirected_edges = []
    for t, u, v in edges:
        if t == 1:
            # Directed edge, add it to the plan
            plan.append(v)
        elif t == 2:
            # Undirected edge, add it to the list of undirected edges
            undirected_edges.append((u, v))
    
    # Sort the undirected edges based on the number of vertices reachable from u
    undirected_edges.sort(key=lambda x: len(reachable_vertices(x[0])), reverse=True)
    
    # Iterate through the sorted undirected edges and add them to the plan
    for u, v in undirected_edges:
        plan.append(v)
    
    return plan

def min_plan():
    # Initialize the plan with the starting vertex
    plan = [s]
    undirected_edges = []
    for t, u, v in edges:
        if t == 1:
            # Directed edge, add it to the plan
            plan.append(v)
        elif t == 2:
            # Undirected edge, add it to the list of undirected edges
            undirected_edges.append((u, v))
    
    # Sort the undirected edges based on the number of vertices reachable from u
    undirected_edges.sort(key=lambda x: len(reachable_vertices(x[0])))
    
    # Iterate through the sorted undirected edges and add them to the plan
    for u, v in undirected_edges:
        plan.append(v)
    
    return plan

def reachable_vertices(start):
    # Initialize the set of reachable vertices with the starting vertex
    reachable = set([start])
    queue = [start]
    
    # Breadth-first search to find all reachable vertices
    while queue:
        vertex = queue.pop(0)
        for t, u, v in edges:
            if t == 1 and v == vertex:
                # Found a directed edge from an already reachable vertex, add it to the queue
                queue.append(u)
            elif t == 2 and (u == vertex or v == vertex):
                # Found an undirected edge from an already reachable vertex, add it to the reachable set
                reachable.add(u)
                reachable.add(v)
    
    return reachable

print(len(max_plan()))
print(''.join(['+' if t == 2 and s == 1 else '-' for t, u, v in edges]))
print(len(min_plan()))
print(''.join(['+' if t == 2 and s == 1 else '-' for t, u, v in edges]))


