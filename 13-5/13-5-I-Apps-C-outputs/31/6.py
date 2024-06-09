
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    return N, a

def smash_multiples(N, a, x):
    smashed = set()
    for i in range(x, N+1, x):
        if i in a:
            smashed.add(i)
    return smashed

def get_earned(N, a, smashed):
    earned = 0
    for i in range(1, N+1):
        if i not in smashed:
            earned += a[i-1]
    return earned

def solve(N, a):
    max_earned = 0
    for x in range(1, N+1):
        smashed = smash_multiples(N, a, x)
        earned = get_earned(N, a, smashed)
        if earned > max_earned:
            max_earned = earned
    return max_earned

if __name__ == '__main__':
    N, a = get_input()
    print(solve(N, a))

