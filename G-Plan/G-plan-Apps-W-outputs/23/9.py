
def longest_segment(n, k, colors):
    color_indices = {}
    left, right = 0, 0
    max_length = 0

    while right < n:
        if colors[right] in color_indices and color_indices[colors[right]] >= left:
            left = color_indices[colors[right]] + 1
        color_indices[colors[right]] = right
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

if __name__ == '__main__':
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    print(longest_segment(n, k, colors))
