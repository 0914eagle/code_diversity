
n = int(input())
temperatures = list(map(int, input().split()))

if temperatures[0] == temperatures[1]:
    print(temperatures[-1])
else:
    if temperatures[1] - temperatures[0] == temperatures[-1] - temperatures[-2]:
        print(temperatures[-1] + (temperatures[-1] - temperatures[-2]))
    else:
        print(temperatures[-1])
