
def is_elegant(n):
    k = 1
    while n % 2 == 0:
        n //= 2
        k *= 2
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        while n % p == 0:
            n //= p
            k *= p
    return k == 1

def count_elegant(n):
    count = 0
    for i in range(2, n+1):
        if is_elegant(i):
            count += 1
    return count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(count_elegant(n))

