alindrome(colors):
    return colors == colors[::-1]

def buy_suits(n, a, b, colors):
    total_cost = 0
    for i in range(n // 2):
        if colors[i] == 2 and colors[n - 1 - i] == 2:
            total_cost += min(a, b)
        elif colors[i] == 2:
            total_cost += b if colors[n - 1 - i] == 0 else a
        elif colors[n - 1 - i] == 2:
            total_cost += a if colors[i] == 0 else b
        elif colors[i] != colors[n - 1 - i]:
            return -1
    return total_cost

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))
    
    result = buy_suits(n, a, b, colors)
    print(result)
