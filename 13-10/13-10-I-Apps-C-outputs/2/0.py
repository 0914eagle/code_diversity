
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x_root = find_parent(x)
    y_root = find_parent(y)
    if x_root != y_root:
        parent[y_root] = x_root

def is_same_set(x, y):
    return find_parent(x) == find_parent(y)

def main():
    n, q = map(int, input().split())
    parent = [i for i in range(n)]
    for _ in range(q):
        query = input().split()
        if query[0] == "?":
            x, y = map(int, query[1:])
            print("yes" if is_same_set(x, y) else "no")
        else:
            x, y = map(int, query[1:])
            union(x, y)

if __name__ == '__main__':
    main()

