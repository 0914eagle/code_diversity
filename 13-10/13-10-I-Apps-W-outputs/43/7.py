
def get_ancestors(p, n):
    ancestors = []
    current = p
    while current != -1:
        ancestors.append(current)
        current = p[current]
    return ancestors

def get_children(c, n):
    children = []
    for i in range(1, n+1):
        if c[i] == 1:
            children.append(i)
    return children

def get_vertices_to_delete(p, c, n):
    vertices_to_delete = []
    for i in range(1, n+1):
        if c[i] == 1 and i not in get_ancestors(p, n) and not any(j in get_children(c, n) for j in get_ancestors(p, n)):
            vertices_to_delete.append(i)
    return vertices_to_delete

def delete_vertices(p, c, n):
    vertices_to_delete = get_vertices_to_delete(p, c, n)
    if len(vertices_to_delete) == 0:
        return [-1]
    else:
        return vertices_to_delete

def main():
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(*delete_vertices(p, c, n))

if __name__ == '__main__':
    main()

