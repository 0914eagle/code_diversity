
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            result += a[i] * b[j]
    return result

def find_smallest_a(n):
    a = 1
    while True:
        if carryless_multiplication(a, a) == n:
            return a
        a += 1
    return -1

if __name__ == '__main__':
    n = int(input())
    print(find_smallest_a(n))

