
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
    count_dict = {}
    for i in range(1, n+1):
        p = path(i)
        for num in p:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
    
    max_value = 0
    for key, value in count_dict.items():
        if value >= k:
            max_value = max(max_value, key)
    
    return max_value

n, k = map(int, input().split())
print(max_value_in_k_paths(n, k))
