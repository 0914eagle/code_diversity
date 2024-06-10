
def get_lex_order(perm):
    
    N = len(perm)
    order = 1
    for i in range(N):
        for j in range(i+1, N):
            if perm[i] > perm[j]:
                order += 1
    return order

def get_abs_diff(perm1, perm2):
    
    return abs(get_lex_order(perm1) - get_lex_order(perm2))

def main():
    N = int(input())
    perm1 = list(map(int, input().split()))
    perm2 = list(map(int, input().split()))
    print(get_abs_diff(perm1, perm2))

if __name__ == '__main__':
    main()

