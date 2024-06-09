
def get_maximum_factories(states, raw_material_sites, factories, transportation_companies):
    # Initialize a graph with a node for each state
    graph = [[] for _ in range(len(states))]

    # Add edges to the graph based on the transportation companies
    for company in transportation_companies:
        for state in company[1:]:
            graph[states.index(state)].append(company[0])

    # Find the factories that can be supplied
    supplied_factories = set()
    for factory in factories:
        factory_index = states.index(factory)
        for state in graph[factory_index]:
            if state in raw_material_sites:
                supplied_factories.add(factory)
                break

    return len(supplied_factories)

