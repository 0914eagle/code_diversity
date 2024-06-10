alindrome(colors):
    return colors == colors[::-1]

def min_cost_palindrome(n, a, b, colors):
    left = 0
    right = n - 1
    cost = 0

    while left < right:
        if colors[left] == 2 and colors[right] == 2:
            cost += min(a, b)
        elif colors[left] == 2:
            cost += b if colors[right] == 0 else 0
        elif colors[right] == 2:
            cost += a if colors[left] == 0 else 0
        elif colors[left] != colors[right]:
            return -1
        
        left += 1
        right -= 1

    return cost

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))

    result = min_cost_palindrome(n, a, b, colors)
    print(result)
