
def find_shortest_cycle(files):
    # Initialize a graph with the given files as nodes
    graph = {}
    for file in files:
        graph[file] = set()

    # Add edges to the graph based on the import statements
    for file in files:
        imports = files[file]
        for import_file in imports:
            graph[file].add(import_file)

    # Find a cycle in the graph
    for file in files:
        if file in graph[file]:
            return file

    # If no cycle is found, return "SHIP IT"
    return "SHIP IT"

