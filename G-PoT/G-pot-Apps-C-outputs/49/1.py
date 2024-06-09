
def count_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    street_set = set(street)
    
    for i in range(N):
        for j in range(1, N-i+1):
            subsequence = street[i:i+j]
            if subsequence not in tile_patterns and set(subsequence).isdisjoint(street_set):
                untileable_cells += 1
    
    return untileable_cells

# Input parsing
N = int(input())
street = input().strip()
M = int(input())
tile_patterns = set()
for _ in range(M):
    tile_patterns.add(input().strip())

# Calculate and output the number of untileable cells
print(count_untileable_cells(N, street, M, tile_patterns))
