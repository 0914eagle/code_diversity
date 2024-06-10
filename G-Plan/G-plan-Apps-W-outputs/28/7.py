alindrome(colors):
    return colors == colors[::-1]

def find_min_cost(n, a, b, colors):
    left = 0
    right = n - 1
    total_cost = 0

    while left < right:
        if colors[left] == 2 and colors[right] == 2:
            total_cost += min(a, b)
        elif colors[left] == 2:
            total_cost += a if colors[right] == 0 else b
        elif colors[right] == 2:
            total_cost += a if colors[left] == 0 else b
        elif colors[left] != colors[right]:
            return -1

        left += 1
        right -= 1

    return total_cost

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))

    result = find_min_cost(n, a, b, colors)
    print(result)
