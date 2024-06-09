
n = int(input())
temperatures = list(map(int, input().split()))

if temperatures[1] - temperatures[0] == temperatures[2] - temperatures[1]:
    diff = temperatures[1] - temperatures[0]
    next_temp = temperatures[-1] + diff
else:
    next_temp = temperatures[-1]

print(next_temp)
