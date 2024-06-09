
def find_shortest_cycle(dependencies):
    
    visited = set()
    cycle = []
    for file in dependencies:
        if file not in visited:
            visited.add(file)
            cycle = find_cycle(file, dependencies, visited, cycle)
            if len(cycle) > 0:
                break
    return cycle

def find_cycle(file, dependencies, visited, cycle):
    
    if file in visited:
        cycle.append(file)
        return cycle
    visited.add(file)
    for imported_file in dependencies[file]:
        cycle = find_cycle(imported_file, dependencies, visited, cycle)
        if len(cycle) > 0:
            break
    return cycle

def main():
    num_files = int(input())
    dependencies = {}
    for _ in range(num_files):
        file = input()
        num_imports = int(input())
        imports = input().split(', ')
        dependencies[file] = imports
    cycle = find_shortest_cycle(dependencies)
    if len(cycle) == 0:
        print("SHIP IT")
    else:
        print(" ".join(cycle))

if __name__ == '__main__':
    main()

