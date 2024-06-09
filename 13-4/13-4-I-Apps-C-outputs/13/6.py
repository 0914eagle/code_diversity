
def get_maximum_number_of_factories(states, raw_material_sites, factories, transportation_companies):
    # Initialize a graph with the states as nodes
    graph = {}
    for state in states:
        graph[state] = []

    # Add edges to the graph based on the transportation companies
    for company in transportation_companies:
        for state in company[1:]:
            graph[company[0]].append(state)

    # Find all possible paths from each raw material site to each factory
    paths = []
    for raw_material_site in raw_material_sites:
        for factory in factories:
            paths.append(find_path(graph, raw_material_site, factory))

    # Count the number of unique factories that can be supplied
    supplied_factories = set()
    for path in paths:
        if path:
            supplied_factories.add(path[-1])

    return len(supplied_factories)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

