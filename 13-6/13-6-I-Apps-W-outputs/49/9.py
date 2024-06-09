
def get_permutation(n):
    permutation = list(map(int, input().split()))
    return permutation

def get_cycles(permutation):
    cycles = []
    visited = set()
    for i in range(len(permutation)):
        if i not in visited:
            cycle = [i]
            j = permutation[i]
            while j not in visited:
                visited.add(j)
                cycle.append(j)
                j = permutation[j]
            cycles.append(cycle)
    return cycles

def print_cycles(cycles):
    print(len(cycles))
    for cycle in cycles:
        print(*cycle)

if __name__ == '__main__':
    n = int(input())
    permutation = get_permutation(n)
    cycles = get_cycles(permutation)
    print_cycles(cycles)

