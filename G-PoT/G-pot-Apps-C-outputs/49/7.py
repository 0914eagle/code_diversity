
def count_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    tile_set = set(tile_patterns)
    
    for i in range(N):
        for j in range(1, min(5001, N-i+1)):
            if street[i:i+j] not in tile_set:
                untileable_cells += 1
    
    return untileable_cells

# Read input
N = int(input())
street = input().strip()
M = int(input())
tile_patterns = set(input().strip() for _ in range(M))

# Calculate and print the number of untileable cells
print(count_untileable_cells(N, street, M, tile_patterns))
