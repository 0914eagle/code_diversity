
def find_longest_segment(n, k, colors):
    color_last_seen = {}
    max_length = 0
    start = 0

    for end in range(n):
        if colors[end] not in color_last_seen or color_last_seen[colors[end]] < start:
            max_length = max(max_length, end - start + 1)
        else:
            start = color_last_seen[colors[end]] + 1
        color_last_seen[colors[end]] = end

    return max_length

if __name__ == '__main__':
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    result = find_longest_segment(n, k, colors)
    print(result)
