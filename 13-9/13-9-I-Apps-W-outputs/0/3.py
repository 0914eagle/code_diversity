
def dfs(tree, start, visited, min_grade):
    if start in visited:
        return
    visited.add(start)
    min_grade[0] = min(min_grade[0], tree[start])
    for neighbor in tree[start]:
        dfs(tree, neighbor, visited, min_grade)

def max_grade(n, k, a):
    tree = {i: set() for i in range(1, n + 1)}
    for i in range(1, n):
        u, v = map(int, input().split())
        tree[u].add(v)
        tree[v].add(u)

    min_grade = [float('inf')]
    dfs(tree, 1, set(), min_grade)
    return min_grade[0]

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_grade(n, k, a))

