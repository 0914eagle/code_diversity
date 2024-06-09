
def count_untileable_cells(N, street, M, tile_patterns):
    untileable_cells = 0
    street_set = set(street)
    
    for i in range(N):
        if street[i] not in street_set:
            untileable_cells += 1
        else:
            for pattern in tile_patterns:
                if i + len(pattern) <= N and street[i:i+len(pattern)] == pattern:
                    break
            else:
                untileable_cells += 1
    
    return untileable_cells

# Input parsing
N = int(input())
street = input().strip()
M = int(input())
tile_patterns = [input().strip() for _ in range(M)]

# Call the function and print the output
print(count_untileable_cells(N, street, M, tile_patterns))
