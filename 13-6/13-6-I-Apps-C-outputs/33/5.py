
def carryless_multiplication(a, b):
    c = 0
    for i in range(len(a)):
        for j in range(len(b)):
            c += a[i] * b[j]
    return c % 10

def find_smallest_positive_integer(N):
    a = 1
    while True:
        if carryless_multiplication(a, a) == N:
            return a
        a += 1
    return -1

if __name__ == '__main__':
    N = int(input())
    print(find_smallest_positive_integer(N))

