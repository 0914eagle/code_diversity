
def find_longest_segment(n, k, colors):
    color_index = {}
    max_length = 0
    start = 0

    for end in range(n):
        if colors[end] in color_index and color_index[colors[end]] >= start:
            start = color_index[colors[end]] + 1
        color_index[colors[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

if __name__ == "__main__":
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    result = find_longest_segment(n, k, colors)
    print(result)
