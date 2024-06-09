
def get_cycles(permutation):
    n = len(permutation)
    cycles = []
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        cycle = [i]
        j = permutation[i]
        while j not in visited:
            visited.add(j)
            cycle.append(j)
            j = permutation[j]
        cycles.append(cycle)
    return cycles

def main():
    n = int(input())
    permutation = list(map(int, input().split()))
    cycles = get_cycles(permutation)
    print(len(cycles))
    for cycle in cycles:
        print(" ".join(map(str, cycle)))

if __name__ == '__main__':
    main()

