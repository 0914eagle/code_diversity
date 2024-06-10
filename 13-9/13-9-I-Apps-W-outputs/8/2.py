
import sys

def get_input():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    return n, q, tree

def dfs(tree, vertex, parent, counter):
    counter[vertex] += 1
    for child in tree[vertex]:
        if child != parent:
            dfs(tree, child, vertex, counter)

def solve(n, q, tree):
    counter = [0] * (n + 1)
    for _ in range(q):
        p, x = map(int, input().split())
        dfs(tree, p, 0, counter)
        counter[p] += x
    return counter

if __name__ == '__main__':
    n, q, tree = get_input()
    counter = solve(n, q, tree)
    print(*counter[1:], sep=' ')

