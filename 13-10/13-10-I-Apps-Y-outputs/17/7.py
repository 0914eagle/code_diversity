
def get_lex_smallest(permutation, n):
    count = 1
    for i in range(n):
        for j in range(i+1, n):
            if permutation[i] > permutation[j]:
                count += 1
    return count

def get_abs_diff(p, q):
    n = len(p)
    a = get_lex_smallest(p, n)
    b = get_lex_smallest(q, n)
    return abs(a - b)

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(get_abs_diff(p, q))

