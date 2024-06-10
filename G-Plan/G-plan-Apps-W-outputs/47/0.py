
def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def is_swap_free(word1, word2):
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 2:
                return False
    return diff_count == 2

def largest_swap_free_set(words):
    n = len(words)
    parent = [i for i in range(n)]
    rank = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if is_swap_free(words[i], words[j]):
                union(parent, rank, i, j)

    max_size = 0
    count = {}
    for i in range(n):
        root = find_parent(parent, i)
        count[root] = count.get(root, 0) + 1
        max_size = max(max_size, count[root])

    return max_size

if __name__ == '__main__':
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(largest_swap_free_set(words))
