
def input_data():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, edges

def is_reachable(n, edges, target_config):
    visited = set()
    queue = [(1, 0)]
    while queue:
        node, value = queue.pop(0)
        if node == n:
            return value == target_config[n]
        if node in visited:
            continue
        visited.add(node)
        for u, v in edges:
            if u == node:
                queue.append((v, value + target_config[v]))
    return False

def main():
    n, edges = input_data()
    target_config = [0] * (n+1)
    for i in range(1, n+1):
        target_config[i] = float(input())
    if is_reachable(n, edges, target_config):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

