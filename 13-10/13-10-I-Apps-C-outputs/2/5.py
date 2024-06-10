
def parse_input(input_str):
    N, Q = map(int, input_str.split())
    return N, Q

def process_operation(operation):
    op, a, b = operation.split()
    if op == "=":
        union(a, b)
    elif op == "?":
        return are_connected(a, b)

def are_connected(a, b):
    return find_root(a) == find_root(b)

def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])
    return parent[a]

def union(a, b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        parent[b_root] = a_root

if __name__ == '__main__':
    N, Q = parse_input(input())
    parent = [i for i in range(N)]
    for _ in range(Q):
        operation = input()
        print(process_operation(operation))

