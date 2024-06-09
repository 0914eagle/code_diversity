
def get_cycles(permutation):
    n = len(permutation)
    visited = [False] * n
    cycles = []
    for i in range(n):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(permutation[j])
                j = permutation[j] - 1
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

