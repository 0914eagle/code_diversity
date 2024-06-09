
def get_input():
    return int(input())

def solve(N):
    count = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            c = N - a*b
            if a*b + c == N and a > 0 and b > 0 and c > 0:
                count += 1
    return count

def main():
    N = get_input()
    print(solve(N))

if __name__ == '__main__':
    main()

