
def color_string(n, s):
    colors = {}
    color = 1
    for char in s:
        if char not in colors:
            colors[char] = color
            color += 1
    num_colors = max(colors.values())
    color_scheme = [colors[char] for char in s]
    return num_colors, color_scheme

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    res, coloring = color_string(n, s)
    print(res)
    print(" ".join(map(str, coloring)))
