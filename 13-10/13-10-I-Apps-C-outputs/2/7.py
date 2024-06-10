
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x_root = find_parent(x)
    y_root = find_parent(y)
    if x_root != y_root:
        parent[x_root] = y_root

def is_same_set(x, y):
    return find_parent(x) == find_parent(y)

def main():
    parent = [i for i in range(N+1)]
    for _ in range(Q):
        op = input().split()
        if op[0] == '=':
            union(int(op[1]), int(op[2]))
        elif op[0] == '?':
            if is_same_set(int(op[1]), int(op[2])):
                print("yes")
            else:
                print("no")

if __name__ == '__main__':
    N, Q = map(int, input().split())
    main()

