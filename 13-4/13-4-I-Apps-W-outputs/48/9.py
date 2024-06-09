
def f1(player, n, cuboids):
    # Your code here
    return player

def f2(player, n, cuboids):
    # Your code here
    return player

if __name__ == '__main__':
    player = input()
    n = int(input())
    cuboids = []
    for i in range(n):
        x, y, z = map(int, input().split())
        cuboids.append((x, y, z))
    print(f1(player, n, cuboids))

