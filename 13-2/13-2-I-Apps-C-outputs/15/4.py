
def find_shortest_cycle(files):
    # Initialize a dictionary to store the dependencies of each file
    dependencies = {}
    for file in files:
        dependencies[file] = set()

    # Populate the dictionary with the dependencies of each file
    for file in files:
        for dep in files[file]:
            dependencies[file].add(dep)

    # Find the shortest cycle by iterating through the files and checking if they have any dependencies that are also in the list of files
    for file in files:
        for dep in dependencies[file]:
            if dep in files:
                return [file, dep]

    # If no cycle is found, return "SHIP IT"
    return "SHIP IT"

