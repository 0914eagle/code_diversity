
n = int(input())
temperatures = list(map(int, input().split()))

if temperatures[0] == temperatures[1]:
    print(temperatures[-1])
else:
    if temperatures[1] - temperatures[0] == temperatures[2] - temperatures[1]:
        diff = temperatures[1] - temperatures[0]
        print(temperatures[-1] + diff)
    else:
        print(temperatures[-1])
