
def get_max_supplied_factories(states, raw_material_sites, factories, transportation_companies):
    # Initialize a graph to represent the state of Acmania
    graph = {}
    for state in states:
        graph[state] = []

    # Add edges to the graph based on the transportation companies
    for company in transportation_companies:
        for state in company[1:]:
            graph[company[0]].append(state)

    # Initialize a set to keep track of the factories that have been supplied
    supplied_factories = set()

    # Iterate through the factories and try to supply them with raw materials
    for factory in factories:
        # Check if the factory has already been supplied
        if factory in supplied_factories:
            continue

        # Find the raw material site that can supply the factory
        for raw_material_site in raw_material_sites:
            # Check if the raw material site is in the same state as the factory
            if raw_material_site[0] == factory[0]:
                # Add the factory to the set of supplied factories
                supplied_factories.add(factory)
                break
            # Check if the raw material site is connected to the factory via a transportation company
            elif raw_material_site[0] in graph[factory[0]]:
                # Add the factory to the set of supplied factories
                supplied_factories.add(factory)
                break

    # Return the number of supplied factories
    return len(supplied_factories)

