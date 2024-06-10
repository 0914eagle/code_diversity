
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def get_inverse_permutation(permutation):
    inverse_permutation = [0] * len(permutation)
    for i in range(len(permutation)):
        inverse_permutation[permutation[i]-1] = i+1
    return inverse_permutation

def apply_permutation(permutation, q):
    result = [0] * len(permutation)
    for i in range(len(permutation)):
        result[i] = permutation[q[i]-1]
    return result

def is_possible(n, k, q, s):
    permutation = get_permutation(n)
    for i in range(k):
        if permutation == s:
            return False
        q_inv = get_inverse_permutation(q)
        permutation = apply_permutation(permutation, q_inv)
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print("YES") if is_possible(n, k, q, s) else print("NO")

