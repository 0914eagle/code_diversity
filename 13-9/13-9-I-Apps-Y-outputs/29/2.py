
def is_permutation(p):
    n = len(p)
    if n == 0:
        return False
    if n == 1:
        return True
    for i in range(n):
        if p[i] < 1 or p[i] > n:
            return False
        for j in range(i+1, n):
            if p[i] == p[j]:
                return False
    return True

def restore_permutation(n, q):
    if n == 1:
        return [1]
    if n == 2:
        if q[0] == 1:
            return [1, 2]
        else:
            return [-1]
    if n == 3:
        if q[0] == 1 and q[1] == 1:
            return [1, 2, 3]
        elif q[0] == 1 and q[1] == 2:
            return [1, 3, 2]
        elif q[0] == 2 and q[1] == 1:
            return [2, 1, 3]
        elif q[0] == 2 and q[1] == 2:
            return [2, 3, 1]
        elif q[0] == 3 and q[1] == 1:
            return [3, 1, 2]
        elif q[0] == 3 and q[1] == 2:
            return [3, 2, 1]
        else:
            return [-1]
    else:
        for i in range(n):
            for j in range(i+1, n):
                if q[i] + q[j] == n:
                    p = [i+1, j+1]
                    break
        if p == []:
            return [-1]
        else:
            return restore_permutation(n-1, q[1:]) + p

def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(restore_permutation(n, q))

if __name__ == '__main__':
    main()

