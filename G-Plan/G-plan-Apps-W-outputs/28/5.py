alindrome(colors):
    return colors == colors[::-1]

def minimal_cost(n, a, b, colors):
    total_cost = 0
    for i in range(n // 2):
        if colors[i] == 2 and colors[n - i - 1] == 2:
            total_cost += min(a, b) * 2
        elif colors[i] == 2:
            total_cost += b if colors[n - i - 1] == 0 else a
        elif colors[n - i - 1] == 2:
            total_cost += b if colors[i] == 0 else a
        elif colors[i] != colors[n - i - 1]:
            return -1
    return total_cost

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    colors = list(map(int, input().split()))
    
    result = minimal_cost(n, a, b, colors)
    print(result) 
