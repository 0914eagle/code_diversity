
def get_ancestors(p, ancestors):
    if p != -1:
        ancestors.append(p)
        get_ancestors(p_i, ancestors)
    return ancestors

def get_descendants(i, descendants):
    for child in children[i]:
        descendants.append(child)
        get_descendants(child, descendants)
    return descendants

def get_non_respecting_vertices(c_i, p_i):
    non_respecting_vertices = []
    if c_i == 1:
        non_respecting_vertices.append(i)
    return non_respecting_vertices

def get_deletion_order(n, p_i, c_i):
    ancestors = []
    descendants = []
    non_respecting_vertices = []
    for i in range(1, n+1):
        get_ancestors(p_i[i], ancestors)
        get_descendants(i, descendants)
        non_respecting_vertices.extend(get_non_respecting_vertices(c_i[i], p_i[i]))
    non_respecting_vertices = sorted(non_respecting_vertices)
    return non_respecting_vertices

def main():
    n = int(input())
    p_i = [int(i) for i in input().split()]
    c_i = [int(i) for i in input().split()]
    non_respecting_vertices = get_deletion_order(n, p_i, c_i)
    if non_respecting_vertices:
        print(*non_respecting_vertices)
    else:
        print(-1)

if __name__ == '__main__':
    main()

