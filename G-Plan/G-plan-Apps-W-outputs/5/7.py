
def min_socks_color_changes(n, m, k, socks_colors, daily_instructions):
    color_changes = 0
    color_pairs = {}
    
    for l, r in daily_instructions:
        if socks_colors[l-1] != socks_colors[r-1]:
            pair = (socks_colors[l-1], socks_colors[r-1])
            color_pairs[pair] = color_pairs.get(pair, 0) + 1
    
    for pair, count in color_pairs.items():
        color_changes += count
    
    return color_changes

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    socks_colors = list(map(int, input().split()))
    daily_instructions = [list(map(int, input().split())) for _ in range(m)]
    
    result = min_socks_color_changes(n, m, k, socks_colors, daily_instructions)
    print(result)
