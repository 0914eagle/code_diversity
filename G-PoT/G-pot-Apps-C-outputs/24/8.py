
n = int(input())

if n % 4 == 0:
    print(n)
    for i in range(1, n+1, 4):
        print(i, i+2, i+1, i+4, i+3, end=' ')
else:
    print(n-1)
    print(0, end=' ')
    for i in range(2, n+1, 4):
        print(i, i+2, i+1, i+4, i+3, end=' ')
