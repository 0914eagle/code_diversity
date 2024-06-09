
def count_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    street_set = set(street)
    
    for i in range(N):
        for pattern in tile_patterns:
            if street[i:i+len(pattern)] == pattern:
                untileable_cells += len(pattern)
                break
    
    return N - untileable_cells

# Read input
N = int(input())
street = input().strip()
M = int(input())
tile_patterns = [input().strip() for _ in range(M)]

# Call the function and print the output
print(count_untileable_cells(N, street, M, tile_patterns))
