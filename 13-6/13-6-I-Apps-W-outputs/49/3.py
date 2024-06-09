
def get_cycles(permutation):
    n = len(permutation)
    cycles = []
    for i in range(n):
        if i not in cycles:
            cycle = [i]
            j = permutation[i]
            while j not in cycle:
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

