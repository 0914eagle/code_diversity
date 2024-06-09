
n = int(input())

if n == 2:
    print(1)
else:
    games = 1
    while n > 1:
        n = (n + 1) // 2
        games += 1
    
    print(games)
