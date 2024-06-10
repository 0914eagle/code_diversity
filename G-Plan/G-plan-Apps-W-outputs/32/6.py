
def calculate_xor_sum(u, v):
    if u == 0 and v == 0:
        return [0]
    if u == 0 or u > v or (v - u) % 2 != 0:
        return [-1]
    
    n = 1
    while n * (n + 1) // 2 <= v:
        if (v - n * (n + 1) // 2) % 2 == 0:
            break
        n += 1
    
    if n * (n + 1) // 2 > v:
        return [-1]
    
    arr = [0] * n
    for i in range(n):
        arr[i] = (u >> i) & 1
    
    for i in range(n):
        if arr[i] == 0:
            if (v - n + i) >= 0:
                arr[i] = n - 1 + i
                v -= n - 1 + i
            else:
                arr[i] = n + i
                v -= n + i
    
    return arr

if __name__ == "__main__":
    u, v = map(int, input().split())
    result = calculate_xor_sum(u, v)
    if result[0] == -1:
        print(-1)
    else:
        print(len(result))
        print(*result)
