
def get_union_find(n):
    parents = [i for i in range(n)]
    sizes = [1] * n
    def find(x):
        if parents[x] == x:
            return x
        else:
            parents[x] = find(parents[x])
            return parents[x]
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return
        if sizes[x_root] < sizes[y_root]:
            parents[x_root] = y_root
            sizes[y_root] += sizes[x_root]
        else:
            parents[y_root] = x_root
            sizes[x_root] += sizes[y_root]
    return find, union

def process_queries(queries):
    n, q = map(int, queries[0].split())
    find, union = get_union_find(n)
    for query in queries[1:]:
        if query.startswith('?'):
            x, y = map(int, query.split()[1:])
            if find(x) == find(y):
                print('yes')
            else:
                print('no')
        else:
            x, y = map(int, query.split()[1:])
            union(x, y)

if __name__ == '__main__':
    queries = [line.strip() for line in sys.stdin]
    process_queries(queries)

