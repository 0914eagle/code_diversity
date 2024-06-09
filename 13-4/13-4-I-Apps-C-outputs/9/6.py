
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(str(a))):
        for j in range(len(str(b))):
            result += int(str(a)[-i-1]) * int(str(b)[-j-1])
        result %= 10
    return result

def find_smallest_positive_integer(n):
    for i in range(1, 1000000000):
        if carryless_multiplication(i, i) == n:
            return i
    return -1

n = int(input())
print(find_smallest_positive_integer(n))

