
def find_beautiful_divisor(n):
    for i in range(1, n+1):
        if n % i == 0:
            if (i + 1) & i == 0:
                return i

n = int(input())
print(find_beautiful_divisor(n))
