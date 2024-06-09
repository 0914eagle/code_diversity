
N = int(input())

if N == 1:
    print(0.0)
else:
    result = 1 - 1/2
    for i in range(2, N+1):
        result *= (i - 1) / i
    print("{:.8f}".format(1 - result))
