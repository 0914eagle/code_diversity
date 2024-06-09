
def count_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    tile_patterns_set = set(tile_patterns)
    
    for i in range(N):
        for j in range(i, N):
            if street[i:j+1] not in tile_patterns_set:
                untileable_cells += 1
    
    return untileable_cells

# Read input
N = int(input())
street = input().strip()
M = int(input())
tile_patterns = [input().strip() for _ in range(M)]

# Call the function and print the output
print(count_untileable_cells(N, street, M, tile_patterns))
