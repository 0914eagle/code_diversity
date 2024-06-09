
n = int(input())

if n == 2:
    print(1)
else:
    games = 1
    while n % 2 == 0:
        n //= 2
        games += 1
    print(games)
