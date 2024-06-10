
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def get_allowed_swaps(m):
    allowed_swaps = []
    for i in range(m):
        a, b = map(int, input().split())
        allowed_swaps.append((a, b))
    return allowed_swaps

def get_min_swaps(permutation, allowed_swaps):
    n = len(permutation)
    visited = [False] * (n+1)
    queue = [(0, permutation)]
    while queue:
        dist, permutation = queue.pop(0)
        if visited[permutation[0]]:
            continue
        visited[permutation[0]] = True
        for a, b in allowed_swaps:
            if permutation[a-1] != a and permutation[b-1] != b:
                new_permutation = list(permutation)
                new_permutation[a-1], new_permutation[b-1] = permutation[b-1], permutation[a-1]
                queue.append((dist+1, new_permutation))
    return dist

def main():
    n, m = map(int, input().split())
    permutation = get_permutation(n)
    allowed_swaps = get_allowed_swaps(m)
    print(get_min_swaps(permutation, allowed_swaps))

if __name__ == '__main__':
    main()

