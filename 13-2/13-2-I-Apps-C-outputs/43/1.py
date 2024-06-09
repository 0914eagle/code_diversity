
def find_shortest_cycle(dependencies):
    
    visited = set()
    cycle = []
    for file in dependencies:
        if file not in visited:
            visited.add(file)
            cycle.append(file)
            dependencies[file] = dependencies[file][1:]
            while len(dependencies[file]) > 0:
                visited.add(dependencies[file][0])
                cycle.append(dependencies[file][0])
                dependencies[file] = dependencies[file][1:]
            if len(cycle) > 1:
                return cycle
    return []

def eliminate_cycles(dependencies):
    
    visited = set()
    while True:
        cycle = find_shortest_cycle(dependencies)
        if len(cycle) == 0:
            break
        for file in cycle:
            dependencies[file] = [x for x in dependencies[file] if x not in cycle]
    return dependencies

def main():
    num_files = int(input())
    files = [input() for _ in range(num_files)]
    dependencies = {}
    for file in files:
        num_imports = int(input())
        imports = [input() for _ in range(num_imports)]
        dependencies[file] = imports
    dependencies = eliminate_cycles(dependencies)
    if len(dependencies) == 0:
        print("SHIP IT")
    else:
        print(*dependencies.keys(), sep="\n")

if __name__ == '__main__':
    main()

