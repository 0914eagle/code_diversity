
def read_input():
    N, C = map(int, input().split())
    programs = []
    for _ in range(N):
        s, t, c = map(int, input().split())
        programs.append((s, t, c))
    return N, C, programs

def solve(N, C, programs):
    channels = [0] * (C + 1)
    for s, t, c in programs:
        channels[c] += t - s
    return sum(1 for x in channels if x > 0)

def main():
    N, C, programs = read_input()
    print(solve(N, C, programs))

if __name__ == '__main__':
    main()

