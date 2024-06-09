
def compute_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    street_set = set(street)
    
    for i in range(N):
        if street[i] not in street_set:
            untileable_cells += 1
        for pattern in tile_patterns:
            if i + len(pattern) <= N and street[i:i+len(pattern)] == pattern:
                street_set.update(pattern)
    
    return untileable_cells

# Read input
N = int(input())
street = input().strip()
M = int(input())
tile_patterns = [input().strip() for _ in range(M)]

# Compute and print the number of untileable cells
print(compute_untileable_cells(N, street, M, tile_patterns))
