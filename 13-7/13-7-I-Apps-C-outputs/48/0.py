
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def apply_permutation(permutation, q):
    n = len(permutation)
    result = [0] * n
    for i in range(n):
        result[i] = permutation[q[i]-1]
    return result

def is_possible(n, k, q, s):
    permutation = get_permutation(n)
    for i in range(k):
        coin = input("Heads or Tails? ")
        if coin == "Heads":
            permutation = apply_permutation(permutation, q)
        else:
            permutation = apply_permutation(permutation, [i+1 for i in range(n)])
    return permutation == s

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print("YES") if is_possible(n, k, q, s) else print("NO")

