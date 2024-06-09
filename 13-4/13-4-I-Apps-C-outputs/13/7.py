
def get_max_supplied_factories(states, raw_material_sites, factories, transportation_companies):
    # Initialize a graph with a node for each state
    graph = {}
    for state in states:
        graph[state] = set()

    # Add edges to the graph based on the transportation companies
    for company in transportation_companies:
        for state in company[1:]:
            graph[company[0]].add(state)

    # Find all possible paths from each raw material site to each factory
    paths = {}
    for raw_material_site in raw_material_sites:
        paths[raw_material_site] = {}
        for factory in factories:
            paths[raw_material_site][factory] = []
            for state in graph[raw_material_site]:
                if state in graph[factory]:
                    paths[raw_material_site][factory].append(state)

    # Count the number of factories that can be supplied from each raw material site
    supplied_factories = {}
    for raw_material_site in raw_material_sites:
        supplied_factories[raw_material_site] = 0
        for factory in factories:
            if len(paths[raw_material_site][factory]) > 0:
                supplied_factories[raw_material_site] += 1

    # Return the maximum number of factories that can be supplied
    return max(supplied_factories.values())

