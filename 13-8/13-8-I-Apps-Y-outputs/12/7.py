
def get_minimum_moves(a, k):
    n = len(a)
    x = 0
    moves = 0
    while True:
        done = True
        for i in range(n):
            if a[i] % k != 0:
                done = False
                break
        if done:
            return moves
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                moves += 1
        x += 1

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_minimum_moves(a, k))

if __name__ == '__main__':
    main()

