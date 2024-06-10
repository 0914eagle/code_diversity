
def find_longest_segment(n, k, colors):
    last_seen = {}
    start = 0
    max_length = 0
    
    for end in range(n):
        if colors[end] in last_seen and last_seen[colors[end]] >= start:
            start = last_seen[colors[end]] + 1
        last_seen[colors[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

if __name__ == "__main__":
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    result = find_longest_segment(n, k, colors)
    print(result)
