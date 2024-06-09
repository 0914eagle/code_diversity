
def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x - 1

def path(x):
    result = [x]
    while x != 1:
        x = f(x)
        result.append(x)
    return result

def max_value_in_k_paths(n, k):
    frequency = {}
    for i in range(1, n+1):
        p = path(i)
        for num in p:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    
    max_value = max([key for key, value in frequency.items() if value >= k])
    return max_value

n, k = map(int, input().split())
print(max_value_in_k_paths(n, k))
