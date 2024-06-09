
n = int(input())
temperatures = list(map(int, input().split()))

if temperatures[1] - temperatures[0] == temperatures[2] - temperatures[1]:
    next_temperature = temperatures[-1] + (temperatures[1] - temperatures[0])
else:
    next_temperature = temperatures[-1]

print(next_temperature)
