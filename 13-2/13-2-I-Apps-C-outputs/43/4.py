
def find_shortest_cycle(dependencies):
    
    visited = set()
    cycle = []
    for file in dependencies:
        if file not in visited:
            if find_cycle(file, dependencies, visited, cycle):
                return cycle
    return None

def find_cycle(file, dependencies, visited, cycle):
    
    if file in visited:
        return True
    visited.add(file)
    for dep in dependencies[file]:
        if dep in cycle:
            return True
        if find_cycle(dep, dependencies, visited, cycle + [file]):
            return True
    return False

def main():
    num_files = int(input())
    dependencies = {}
    for _ in range(num_files):
        file = input()
        num_imports = int(input())
        imports = input().split(', ')
        dependencies[file] = imports
    cycle = find_shortest_cycle(dependencies)
    if cycle:
        print(' '.join(cycle))
    else:
        print('SHIP IT')

if __name__ == '__main__':
    main()

