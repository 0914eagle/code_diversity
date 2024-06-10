alindrome(colors):
    return colors == colors[::-1]

def minimal_cost(n, a, b, colors):
    left, right = 0, n - 1
    cost = 0

    while left < right:
        if colors[left] == 2 and colors[right] == 2:
            cost += min(a, b)
        elif colors[left] == 2:
            cost += a if colors[right] == 0 else b
        elif colors[right] == 2:
            cost += a if colors[left] == 0 else b
        elif colors[left] != colors[right]:
            return -1

        left += 1
        right -= 1

    return cost

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))

    result = minimal_cost(n, a, b, colors)
    print(result