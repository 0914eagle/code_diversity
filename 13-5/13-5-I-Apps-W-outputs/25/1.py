
def f1(n):
    return len(bin(n)[2:])

def f2(n):
    count = 0
    while n > 0:
        count += 1
        n &= n - 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(f1(n))
    print(f2(n))

