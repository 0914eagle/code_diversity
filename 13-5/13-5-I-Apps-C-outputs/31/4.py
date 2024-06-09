
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    return N, a

def smash_multiples(N, a, x):
    smashed = set()
    for i in range(x, N+1, x):
        if i in smashed:
            continue
        smashed.add(i)
        a[i-1] = 0
    return a

def get_earned(a):
    earned = 0
    for i in range(len(a)):
        if a[i] > 0:
            earned += a[i]
    return earned

def solve(N, a):
    max_earned = 0
    for x in range(1, N+1):
        earned = get_earned(smash_multiples(N, a, x))
        if earned > max_earned:
            max_earned = earned
    return max_earned

if __name__ == '__main__':
    N, a = get_input()
    print(solve(N, a))

