
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(b)):
        result += a * int(b[i])
    return result

def find_square_root(n):
    for i in range(1, n+1):
        if i * i == n:
            return i
    return -1

n = int(input())
result = find_square_root(n)
if result == -1:
    print(-1)
else:
    print(result)

