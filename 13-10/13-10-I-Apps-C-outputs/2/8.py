
def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union_sets(x, y):
    x_root = find_set(x)
    y_root = find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root

def is_same_set(x, y):
    x_root = find_set(x)
    y_root = find_set(y)
    return x_root == y_root

def main():
    n, q = map(int, input().split())
    parent = [i for i in range(n)]
    for i in range(q):
        query = input().split()
        if query[0] == "?":
            x, y = map(int, query[1:])
            if is_same_set(x, y):
                print("yes")
            else:
                print("no")
        else:
            x, y = map(int, query[1:])
            union_sets(x, y)

if __name__ == '__main__':
    main()

