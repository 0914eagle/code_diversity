
def find_longest_segment(n, k, colors):
    color_indices = {}
    max_length = 0
    left = 0

    for right in range(n):
        color = colors[right]
        if color in color_indices and color_indices[color] >= left:
            left = color_indices[color] + 1
        color_indices[color] = right
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    result = find_longest_segment(n, k, colors)
    print(result)
