
def f1(n):
    return len(str(n))

def f2(n):
    count = 0
    for i in range(1, n+1):
        count += len(str(i))
    return count

if __name__ == '__main__':
    n = int(input())
    print(f2(n))

