
import sys
input = sys.stdin.read().split()

def get_tree(n):
    tree = [[] for _ in range(n+1)]
    for i in range(1, n):
        a, b = map(int, input[i*2-1], input[i*2])
        tree[a].append(b)
        tree[b].append(a)
    return tree

def get_root(tree):
    for i in range(1, len(tree)):
        if not tree[i]:
            return i

def dfs(tree, root, counter):
    counter[root] += 1
    for node in tree[root]:
        if node != root:
            dfs(tree, node, counter)

def solve(n, q):
    tree = get_tree(n)
    root = get_root(tree)
    counter = [0] * (n+1)
    for i in range(q):
        p, x = map(int, input[i*2+n+1], input[i*2+n+2])
        dfs(tree, p, counter)
    return " ".join(map(str, counter))

if __name__ == '__main__':
    n, q = map(int, input[0], input[1])
    print(solve(n, q))

