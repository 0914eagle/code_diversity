socks_color_changes(n, m, k, c, instructions):
    color_changes = 0
    color_pairs = {}
    
    for l, r in instructions:
        if c[l-1] != c[r-1]:
            pair = (c[l-1], c[r-1])
            color_pairs[pair] = color_pairs.get(pair, 0) + 1
    
    for pair, freq in color_pairs.items():
        color_changes += freq
    
    return color_changes

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    c = list(map(int, input().split()))
    instructions = [list(map(int, input().split())) for _ in range(m)]
    
    result = min_socks_color_changes(n, m, k, c, instructions)
    print(result)
