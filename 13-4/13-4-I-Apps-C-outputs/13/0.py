
def get_max_supplied_factories(states, raw_material_sites, factories, transportation_companies):
    # Initialize a graph to represent the supply chain
    graph = {}
    for state in states:
        graph[state] = []

    # Add edges to the graph based on the transportation companies
    for company in transportation_companies:
        for state in company[1:]:
            graph[company[0]].append(state)

    # Find the factories that can be supplied
    supplied_factories = []
    for factory in factories:
        for state in graph[factory]:
            if state in raw_material_sites:
                supplied_factories.append(factory)
                break

    return len(supplied_factories)

