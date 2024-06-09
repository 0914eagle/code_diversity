
def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    count = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            count += 1
            q = pi[q - 1]
    return count

def count_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    for i in range(N):
        for pattern in tile_patterns:
            if kmp_search(street[i:], pattern) > 0:
                break
        else:
            untileable_cells += 1
    return untileable_cells

N = int(input())
street = input().strip()
M = int(input())
tile_patterns = [input().strip() for _ in range(M)]

print(count_untileable_cells(N, street, M, tile_patterns))
