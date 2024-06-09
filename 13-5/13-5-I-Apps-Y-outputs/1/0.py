
def read_data():
    n, m = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    queries = list(map(int, input().split()))
    return n, m, edges, queries

def find_pairs(edges, queries):
    pairs = []
    for u, v, w in edges:
        for q in queries:
            if w <= q:
                pairs.append((u, v))
    return pairs

def count_pairs(pairs, queries):
    counts = []
    for q in queries:
        count = 0
        for u, v in pairs:
            if u < v and v <= q:
                count += 1
        counts.append(count)
    return counts

def main():
    n, m, edges, queries = read_data()
    pairs = find_pairs(edges, queries)
    counts = count_pairs(pairs, queries)
    print(*counts, sep='\n')

if __name__ == '__main__':
    main()

