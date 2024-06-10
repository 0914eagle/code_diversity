
def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, i, j):
    parent_i = find_parent(parent, i)
    parent_j = find_parent(parent, j)

    if parent_i != parent_j:
        if rank[parent_i] < rank[parent_j]:
            parent[parent_i] = parent_j
        elif rank[parent_i] > rank[parent_j]:
            parent[parent_j] = parent_i
        else:
            parent[parent_j] = parent_i
            rank[parent_i] += 1

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
    group_sizes = {}
    for i in range(n):
        root = find_parent(parent, i)
        if root not in group_sizes:
            group_sizes[root] = 1
        else:
            group_sizes[root] += 1
        max_size = max(max_size, group_sizes[root])

    return max_size

if __name__ == '__main__':
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(largest_swap_free_set(words))
