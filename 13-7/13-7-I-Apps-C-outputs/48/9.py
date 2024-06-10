
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def apply_permutation(permutation, q):
    n = len(permutation)
    new_permutation = [0] * n
    for i in range(n):
        new_permutation[i] = permutation[q[i]-1]
    return new_permutation

def check_permutation(p, s):
    n = len(p)
    for i in range(n):
        if p[i] != s[i]:
            return False
    return True

def play_game(n, k, q, s):
    permutation = get_permutation(n)
    for i in range(k):
        coin = input("Heads or Tails? ")
        if coin == "Heads":
            permutation = apply_permutation(permutation, q)
        else:
            permutation = apply_permutation(permutation, [i+1 for i in range(n)])
    return check_permutation(permutation, s)

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    result = play_game(n, k, q, s)
    if result:
        print("YES")
    else:
        print("NO")

