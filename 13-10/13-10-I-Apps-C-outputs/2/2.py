
def read_input():
    N, Q = map(int, input().split())
    operations = []
    for i in range(Q):
        operation = input()
        operations.append(operation)
    return N, Q, operations

def perform_operations(N, Q, operations):
    parents = [-1 for _ in range(N)]
    for operation in operations:
        if operation[0] == '=':
            a, b = map(int, operation[2:].split())
            union(parents, a, b)
        elif operation[0] == '?':
            a, b = map(int, operation[2:].split())
            if find(parents, a) == find(parents, b):
                print("yes")
            else:
                print("no")

def find(parents, x):
    if parents[x] == -1:
        return x
    else:
        return find(parents, parents[x])

def union(parents, x, y):
    x_root = find(parents, x)
    y_root = find(parents, y)
    if x_root != y_root:
        parents[x_root] = y_root

if __name__ == '__main__':
    N, Q, operations = read_input()
    perform_operations(N, Q, operations)

