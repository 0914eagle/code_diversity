
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def apply_permutation(permutation, q):
    n = len(permutation)
    new_permutation = [0] * n
    for i in range(n):
        new_permutation[i] = permutation[q[i]-1]
    return new_permutation

def apply_inverse_permutation(permutation, q):
    n = len(permutation)
    new_permutation = [0] * n
    for i in range(n):
        new_permutation[q[i]-1] = permutation[i]
    return new_permutation

def is_permutation_possible(q, s, k):
    n = len(q)
    permutation = get_permutation(n)
    for i in range(k):
        if permutation == s:
            return False
        coin = random.randint(0, 1)
        if coin == 0:
            permutation = apply_permutation(permutation, q)
        else:
            permutation = apply_inverse_permutation(permutation, q)
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print("YES") if is_permutation_possible(q, s, k) else print("NO")

