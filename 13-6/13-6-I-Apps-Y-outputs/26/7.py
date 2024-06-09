
def get_cost(tree, root):
    cost = 0
    for vertex in tree:
        cost += tree[root][vertex] * vertex
    return cost

def get_maximum_cost(tree):
    maximum_cost = 0
    for root in tree:
        cost = get_cost(tree, root)
        if cost > maximum_cost:
            maximum_cost = cost
    return maximum_cost

def main():
    n = int(input())
    tree = {}
    for i in range(n):
        tree[i+1] = {}
    for i in range(n-1):
        u, v = map(int, input().split())
        tree[u][v] = 1
        tree[v][u] = 1
    print(get_maximum_cost(tree))

if __name__ == '__main__':
    main()

