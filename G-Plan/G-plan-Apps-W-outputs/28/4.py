
def is_palindrome(colors):
    return colors == colors[::-1]

def find_min_cost(n, a, b, colors):
    left = 0
    right = n - 1
    min_cost = 0

    while left < right:
        if colors[left] == 2 and colors[right] == 2:
            min_cost += min(a, b)
        elif colors[left] == 2:
            min_cost += a if colors[right] == 0 else b
        elif colors[right] == 2:
            min_cost += a if colors[left] == 0 else b
        elif colors[left] != colors[right]:
            if colors[left] == 0:
                min_cost += a
            else:
                min_cost += b
        left += 1
        right -= 1

    return min_cost if is_palindrome(colors) else -1

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))
    print(find_min_cost(n, a, b, colors))
