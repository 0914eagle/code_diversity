
def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, i, j):
    i_parent = find_parent(parent, i)
    j_parent = find_parent(parent, j)

    if i_parent != j_parent:
        if rank[i_parent] < rank[j_parent]:
            parent[i_parent] = j_parent
        elif rank[i_parent] > rank[j_parent]:
            parent[j_parent] = i_parent
        else:
            parent[j_parent] = i_parent
            rank[i_parent] += 1

def is_swap_free(w1, w2):
    diff_count = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 2:
                return False
    return diff_count == 2

def largest_swap_free_set_size(N, words):
    parent = [i for i in range(N)]
    rank = [0] * N

    for i in range(N):
        for j in range(i + 1, N):
            if is_swap_free(words[i], words[j]):
                union(parent, rank, i, j)

    max_size = 0
    count = [0] * N
    for i in range(N):
        p = find_parent(parent, i)
        count[p] += 1
        max_size = max(max_size, count[p])

    return max_size

if __name__ == '__main__':
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(largest_swap_free_set_size(N, words))
