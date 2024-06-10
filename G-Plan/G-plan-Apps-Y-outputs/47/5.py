
def min_colors_to_sort_string(n, s):
    colors = [0] * n
    color = 1
    colors[0] = color

    for i in range(1, n):
        if s[i] >= s[i - 1]:
            colors[i] = colors[i - 1]
        else:
            color += 1
            colors[i] = color

    return max(colors), colors

if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    res, coloring = min_colors_to_sort_string(n, s)
    print(res)
    print(' '.join(map(str, coloring)))
