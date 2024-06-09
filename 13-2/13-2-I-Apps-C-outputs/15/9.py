
def find_shortest_cycle(files):
    # Initialize a dictionary to store the dependencies of each file
    dependencies = {}
    for file in files:
        dependencies[file] = set()

    # Populate the dictionary with the dependencies of each file
    for file in files:
        for dep in files[file]:
            dependencies[file].add(dep)

    # Find the shortest cycle by iteratively removing files from the dependency graph
    removed_files = set()
    while True:
        # Find a file with no dependencies that is not already removed
        for file in files:
            if len(dependencies[file]) == 0 and file not in removed_files:
                # Remove the file and its dependencies from the graph
                removed_files.add(file)
                for dep in dependencies:
                    if file in dependencies[dep]:
                        dependencies[dep].remove(file)

                # If the graph has no more cycles, return the removed files in the order they were removed
                if len(removed_files) == len(files):
                    return list(removed_files)

                # If the graph has a cycle, continue removing files until there are no more cycles
                break

        # If the graph has no more files to remove, return "SHIP IT"
        if len(removed_files) == len(files):
            return "SHIP IT"

