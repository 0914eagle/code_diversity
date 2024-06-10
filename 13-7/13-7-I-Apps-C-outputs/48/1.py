
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def apply_permutation(permutation, q):
    n = len(permutation)
    new_permutation = [0] * n
    for i in range(n):
        new_permutation[i] = permutation[q[i]-1]
    return new_permutation

def inverse_permutation(permutation):
    n = len(permutation)
    inverse = [0] * n
    for i in range(n):
        inverse[permutation[i]-1] = i+1
    return inverse

def is_possible(n, k, q, s):
    permutation = get_permutation(n)
    for i in range(k):
        if permutation == s:
            return False
        coin = random.randint(0, 1)
        if coin == 0:
            permutation = apply_permutation(permutation, q)
        else:
            permutation = apply_permutation(permutation, inverse_permutation(q))
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print("YES" if is_possible(n, k, q, s) else "NO")

