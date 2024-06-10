
def read_input():
    N = int(input())
    bricks = list(map(int, input().split()))
    return N, bricks

def solve(N, bricks):
    towers = 0
    for i in range(N):
        if i == 0 or bricks[i] > bricks[i-1]:
            towers += 1
    return towers

def main():
    N, bricks = read_input()
    print(solve(N, bricks))

if __name__ == '__main__':
    main()

