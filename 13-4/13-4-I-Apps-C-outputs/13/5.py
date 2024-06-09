
def get_maximum_factories(states, raw_material_sites, factories, transportation_companies):
    # Initialize a graph to store the supply chain
    graph = {}

    # Add nodes for each state
    for state in states:
        graph[state] = []

    # Add edges for each transportation company
    for company in transportation_companies:
        for state in company[1:]:
            graph[company[0]].append(state)

    # Add edges for each raw material site
    for site in raw_material_sites:
        graph[site].append(site)

    # Add edges for each factory
    for factory in factories:
        graph[factory].append(factory)

    # Find the maximum number of factories that can be supplied
    maximum_factories = 0
    for state in states:
        if len(graph[state]) == 1:
            maximum_factories += 1

    return maximum_factories

