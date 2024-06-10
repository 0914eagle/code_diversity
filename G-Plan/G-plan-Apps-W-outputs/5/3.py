
def min_socks_color_changes(n, m, k, colors, instructions):
    color_changes = 0
    color_pairs = {}
    
    for l, r in instructions:
        if colors[l-1] != colors[r-1]:
            pair = (min(colors[l-1], colors[r-1]), max(colors[l-1], colors[r-1]))
            color_pairs[pair] = color_pairs.get(pair, 0) + 1
    
    for pair, count in color_pairs.items():
        color_changes += count
    
    return color_changes

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    colors = list(map(int, input().split()))
    instructions = [list(map(int, input().split())) for _ in range(m)]
    
    result = min_socks_color_changes(n, m, k, colors, instructions)
    print(result)
