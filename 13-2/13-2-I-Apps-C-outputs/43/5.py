
def find_shortest_cycle(dependencies):
    
    visited = set()
    cycle = []
    for file in dependencies:
        if file not in visited:
            visited.add(file)
            cycle = dfs(file, dependencies, visited, cycle)
            if len(cycle) > 0:
                break
    return cycle

def dfs(file, dependencies, visited, cycle):
    
    visited.add(file)
    cycle.append(file)
    for dep in dependencies[file]:
        if dep not in visited:
            cycle = dfs(dep, dependencies, visited, cycle)
    return cycle

def main():
    n = int(input())
    files = input().split()
    dependencies = {}
    for i in range(n):
        file, k = input().split()
        dependencies[file] = input().split(', ')
    cycle = find_shortest_cycle(dependencies)
    if len(cycle) == 0:
        print("SHIP IT")
    else:
        print(" ".join(cycle))

if __name__ == '__main__':
    main()

