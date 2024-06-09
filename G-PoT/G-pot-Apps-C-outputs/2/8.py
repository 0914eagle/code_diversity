
n = int(input())
temps = list(map(int, input().split()))

if temps[0] == temps[1]:
    print(temps[-1])
else:
    diff = temps[1] - temps[0]
    if all(temps[i] + diff == temps[i+1] for i in range(n-1)):
        print(temps[-1] + diff)
    else:
        print(temps[-1])
