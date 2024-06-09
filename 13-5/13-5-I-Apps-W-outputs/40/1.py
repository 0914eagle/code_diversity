
def f(n):
    result = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            result += i
        else:
            result -= i
    return result

if __name__ == '__main__':
    n = int(input())
    print(f(n))

