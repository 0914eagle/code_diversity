
def can_reach_configuration(tree, configuration):
    # Your code here
    pass

def main():
    n = int(input())
    tree = {}
    for i in range(n-1):
        u, v = map(int, input().split())
        tree[u] = tree.get(u, []) + [v]
        tree[v] = tree.get(v, []) + [u]
    configuration = [float(input()) for _ in range(n-1)]
    if can_reach_configuration(tree, configuration):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

