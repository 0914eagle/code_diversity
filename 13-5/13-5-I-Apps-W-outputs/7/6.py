
def get_mex(S):
    mex = 0
    for i in range(1, max(S) + 1):
        if i not in S:
            mex = i
            break
    return mex

def get_max_strength(n, m, p, c, d, k):
    club_members = [[] for _ in range(m)]
    for i in range(n):
        club_members[c[i] - 1].append(i)
    
    max_strength = [0] * d
    for i in range(d):
        if k[i] != 0:
            club_members[c[k[i] - 1] - 1].remove(k[i] - 1)
        mex = get_mex(club_members[i])
        max_strength[i] = mex
    
    return max_strength

if __name__ == '__main__':
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = int(input())
    k = list(map(int, input().split()))
    max_strength = get_max_strength(n, m, p, c, d, k)
    for i in range(d):
        print(max_strength[i])

