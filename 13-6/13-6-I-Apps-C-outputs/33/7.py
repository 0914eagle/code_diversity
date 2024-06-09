
def carryless_add(a, b):
    return (a + b) % 10

def carryless_multiply(a, b):
    result = 0
    for i in range(len(str(a))):
        for j in range(len(str(b))):
            result = carryless_add(result, carryless_add(a % 10 * b % 10, a // 10 * b // 10))
        a //= 10
    return result

def find_square_root(n):
    for i in range(1, n + 1):
        if carryless_multiply(i, i) == n:
            return i
    return -1

if __name__ == '__main__':
    n = int(input())
    print(find_square_root(n))

