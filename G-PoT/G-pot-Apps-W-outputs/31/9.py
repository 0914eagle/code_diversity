
def find_beautiful_divisor(n):
    for i in range(1, n+1):
        if n % i == 0:
            if (i + 1) & i == 0:
                return i
    return -1

n = int(input())
result = find_beautiful_divisor(n)
print(result)
