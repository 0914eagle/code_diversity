
def get_ancestors(p, ancestors=None):
    if ancestors is None:
        ancestors = []
    if p != -1:
        ancestors.append(p)
        get_ancestors(p, ancestors)
    return ancestors

def get_order(p, c, n):
    order = []
    if c == 1:
        order.append(n)
    elif p != -1:
        order.extend(get_order(p, 0, n))
    return order

def delete_vertices(n, parents, children):
    order = []
    for i in range(n):
        if parents[i] != -1 and children[i] == 0:
            order.extend(get_order(parents[i], 0, i))
    if not order:
        order.append(-1)
    return order

def main():
    n = int(input())
    parents = []
    children = []
    for i in range(n):
        p, c = map(int, input().split())
        parents.append(p)
        children.append(c)
    order = delete_vertices(n, parents, children)
    print(*order)

if __name__ == '__main__':
    main()

