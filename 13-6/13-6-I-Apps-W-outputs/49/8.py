
def get_cycles(permutation):
    cycles = []
    visited = set()
    for i in range(len(permutation)):
        if i not in visited:
            cycle = []
            j = i
            while j not in visited:
                visited.add(j)
                cycle.append(j)
                j = permutation[j] - 1
            cycles.append(cycle)
    return cycles

def main():
    N = int(input())
    permutation = list(map(int, input().split()))
    cycles = get_cycles(permutation)
    print(len(cycles))
    for cycle in cycles:
        print(*cycle)

if __name__ == '__main__':
    main()

