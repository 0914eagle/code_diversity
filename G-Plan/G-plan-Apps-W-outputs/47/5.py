
def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, i, j):
    i_parent = find_parent(parent, i)
    j_parent = find_parent(parent, j)

    if rank[i_parent] < rank[j_parent]:
        parent[i_parent] = j_parent
    elif rank[i_parent] > rank[j_parent]:
        parent[j_parent] = i_parent
    else:
        parent[j_parent] = i_parent
        rank[i_parent] += 1

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

    max_size = max(rank)
    return max_size

if __name__ == '__main__':
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(largest_swap_free_set(words))
