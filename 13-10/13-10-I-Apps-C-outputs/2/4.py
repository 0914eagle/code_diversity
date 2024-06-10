
def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union_set(x, y):
    x_root = find_set(x)
    y_root = find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root

def is_same_set(x, y):
    return find_set(x) == find_set(y)

def main():
    N, Q = map(int, input().split())
    parent = [i for i in range(N)]
    for _ in range(Q):
        query = input().split()
        if query[0] == "=":
            union_set(int(query[1]), int(query[2]))
        elif query[0] == "?":
            if is_same_set(int(query[1]), int(query[2])):
                print("yes")
            else:
                print("no")

if __name__ == '__main__':
    main()

