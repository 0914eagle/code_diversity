
def find_shortest_cycle(dependencies):
    
    # Initialize a set to keep track of the files that have been visited
    visited = set()
    # Initialize a queue to keep track of the files to visit
    queue = []
    # Add the first file to the queue
    queue.append(dependencies.keys())
    # Loop until the queue is empty
    while queue:
        # Get the next file to visit
        file = queue.pop(0)
        # If the file has already been visited, skip it
        if file in visited:
            continue
        # If the file imports any other file, add it to the queue
        if dependencies[file]:
            queue.extend(dependencies[file])
        # Add the file to the visited set
        visited.add(file)
    # If the visited set is equal to the number of files, there are no cycles
    if len(visited) == len(dependencies):
        return None
    # Otherwise, find the shortest cycle by starting from any file that has not been visited
    for file in dependencies:
        if file not in visited:
            break
    # Follow the imports to find the shortest cycle
    cycle = [file]
    while True:
        file = dependencies[file][0]
        if file in cycle:
            break
        cycle.append(file)
    return cycle

def main():
    # Read the number of files and their dependencies from stdin
    num_files = int(input())
    dependencies = {}
    for _ in range(num_files):
        file, num_imports = input().split()
        imports = input().split(', ')
        dependencies[file] = imports
    # Find the shortest cycle in the dependency graph
    cycle = find_shortest_cycle(dependencies)
    # If there is no cycle, print "SHIP IT"
    if not cycle:
        print("SHIP IT")
    # Otherwise, print the names of the files in the cycle
    else:
        print(*cycle)

if __name__ == '__main__':
    main()

