
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            result += a[i] * b[j]
    return result

def find_smallest_positive_integer(n):
    for i in range(1, n):
        if carryless_multiplication(i, i) == n:
            return i
    return -1

n = int(input())
print(find_smallest_positive_integer(n))

