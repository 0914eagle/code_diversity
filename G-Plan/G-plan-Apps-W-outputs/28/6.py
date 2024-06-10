alindrome(colors):
    return colors == colors[::-1]

def buy_suits(n, a, b, colors):
    total_cost = 0
    for i in range(n // 2):
        if colors[i] == 2 and colors[n - i - 1] == 2:
            total_cost += min(a, b) * 2
        elif colors[i] == 2:
            total_cost += b if colors[n - i - 1] == 0 else a
        elif colors[n - i - 1] == 2:
            total_cost += b if colors[i] == 0 else a
        elif colors[i] != colors[n - i - 1]:
            if colors[i] == 0:
                total_cost += a
            else:
                total_cost += b
            colors[i] = colors[n - i - 1] = min(colors[i], colors[n - i - 1])
    
    return total_cost if is_palindrome(colors) else -1

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))
    print(buy_suits(n, a, b, colors))
