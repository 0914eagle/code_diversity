
def min_socks_color_changes(n, m, k, colors, instructions):
    freq = {}
    for l, r in instructions:
        if colors[l-1] != colors[r-1]:
            pair = (colors[l-1], colors[r-1])
            freq[pair] = freq.get(pair, 0) + 1
    
    changes_needed = sum(freq.values())
    return changes_needed

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    colors = list(map(int, input().split()))
    instructions = [list(map(int, input().split())) for _ in range(m)]
    
    result = min_socks_color_changes(n, m, k, colors, instructions)
    print(result)
