
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def apply_permutation(permutation, q):
    n = len(permutation)
    new_permutation = [0] * n
    for i in range(n):
        new_permutation[i] = permutation[q[i]-1]
    return new_permutation

def is_permutation_possible(n, k, q, s):
    permutation = get_permutation(n)
    for i in range(k):
        if permutation == s:
            return False
        permutation = apply_permutation(permutation, q)
    return True

def main():
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print("YES" if is_permutation_possible(n, k, q, s) else "NO")

if __name__ == '__main__':
    main()

