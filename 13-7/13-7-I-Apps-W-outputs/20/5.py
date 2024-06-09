
def get_network_topology(graph):
    n = len(graph)
    m = len(graph[0])
    if m == n-1:
        return "bus topology"
    elif m == n-2:
        return "ring topology"
    elif m == n-3:
        return "star topology"
    else:
        return "unknown topology"

