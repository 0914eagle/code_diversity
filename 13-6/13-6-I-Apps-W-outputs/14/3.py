
def solve(m):
    count = 0
    for n in range(1, 100001):
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        if str(factorial)[-m:] == '0'*m:
            count += 1
    print(count)
    for n in range(1, 100001):
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        if str(factorial)[-m:] == '0'*m:
            print(n)

