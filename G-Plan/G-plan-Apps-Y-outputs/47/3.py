
def color_string(n, s):
    colors = {}
    color = 1
    for char in s:
        if char not in colors:
            colors[char] = color
            color += 1
    return len(colors), [colors[char] for char in s]

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    res, coloring = color_string(n, s)
    print(res)
    print(" ".join(map(str, coloring)))
