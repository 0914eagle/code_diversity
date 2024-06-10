
def longest_segment(n, k, colors):
    color_indices = {}
    max_length = 0
    start = 0

    for i in range(n):
        if colors[i] in color_indices and color_indices[colors[i]] >= start:
            start = color_indices[colors[i]] + 1

        color_indices[colors[i]] = i
        max_length = max(max_length, i - start + 1)

    return max_length

if __name__ == '__main__':
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    print(longest_segment(n, k, colors))
