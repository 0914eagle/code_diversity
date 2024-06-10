
def get_parents(n, parent):
    parents = [0] * (n + 1)
    for i in range(1, n + 1):
        parents[i] = parent[i]
    return parents

def get_paths(n, parents):
    paths = [0] * (n + 1)
    for i in range(1, n + 1):
        paths[i] = 1
    for i in range(2, n + 1):
        paths[i] += paths[parents[i]]
    return paths

def get_swap_pairs(n, paths):
    pairs = set()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and paths[i] == paths[j]:
                pairs.add((i, j))
    return pairs

def main():
    n = int(input())
    a = list(map(int, input().split()))
    parent = list(map(int, input().split()))
    parents = get_parents(n, parent)
    paths = get_paths(n, parents)
    pairs = get_swap_pairs(n, paths)
    print(len(pairs))

if __name__ == '__main__':
    main()

