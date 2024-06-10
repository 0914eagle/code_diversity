
def get_ancestors(p_i, n):
    ancestors = []
    current = p_i
    while current != -1:
        ancestors.append(current)
        current = p_i[current - 1]
    return ancestors

def get_children(c_i, n):
    children = []
    for i in range(1, n + 1):
        if c_i[i] == 1:
            children.append(i)
    return children

def get_order(p_i, c_i, n):
    order = []
    for i in range(1, n + 1):
        if p_i[i] != -1 and c_i[i] == 0:
            order.append(i)
    return order

def delete_vertex(p_i, c_i, n):
    ancestors = get_ancestors(p_i, n)
    children = get_children(c_i, n)
    order = get_order(p_i, c_i, n)
    if len(order) == 0:
        return -1
    vertex = order[0]
    for i in range(1, n + 1):
        if i in ancestors and i not in children:
            p_i[i] = p_i[vertex]
    return vertex

def main():
    n = int(input())
    p_i = list(map(int, input().split()))
    c_i = list(map(int, input().split()))
    while True:
        vertex = delete_vertex(p_i, c_i, n)
        if vertex == -1:
            break
        print(vertex, end=" ")
    print()

if __name__ == '__main__':
    main()

