
def get_input():
    N = int(input())
    S = input()
    return N, S

def solve(N, S):
    x = 0
    for s in S:
        if s == 'I':
            x += 1
        else:
            x -= 1
    return max(x, 0)

def main():
    N, S = get_input()
    print(solve(N, S))

if __name__ == '__main__':
    main()

