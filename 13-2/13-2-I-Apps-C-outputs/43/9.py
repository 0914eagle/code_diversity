
def find_shortest_cycle(dependencies):
    
    visited = set()
    cycle = []
    for file in dependencies:
        if file not in visited:
            visited.add(file)
            cycle.append(file)
            dependencies[file] = [dep for dep in dependencies[file] if dep not in visited]
            if not dependencies[file]:
                return cycle
    return None

def eliminate_cycles(dependencies):
    
    while True:
        cycle = find_shortest_cycle(dependencies)
        if cycle is None:
            break
        for file in cycle:
            dependencies[file] = [dep for dep in dependencies[file] if dep not in cycle]
    return dependencies

def main():
    num_files = int(input())
    files = [input() for _ in range(num_files)]
    dependencies = {}
    for file in files:
        num_deps = int(input())
        deps = [input() for _ in range(num_deps)]
        dependencies[file] = deps
    dependencies = eliminate_cycles(dependencies)
    if all(not deps for deps in dependencies.values()):
        print("SHIP IT")
    else:
        cycle = find_shortest_cycle(dependencies)
        print(*cycle)

if __name__ == '__main__':
    main()

