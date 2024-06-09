
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

n, k = map(int, input().split())

count_dict = {}
for i in range(1, n+1):
    p = path(i)
    for num in p:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

max_value = max([key for key, value in count_dict.items() if value >= k])

print(max_value)
