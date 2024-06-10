
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

def apply_inverse_permutation(permutation, q):
    result = [0] * len(permutation)
    for i in range(len(permutation)):
        result[i] = permutation[q[i]-1]
    return result

def get_coin_tosses(k):
    coin_tosses = []
    for i in range(k):
        coin_tosses.append(i%2)
    return coin_tosses

def get_result(n, k, q, s):
    permutation = get_permutation(n)
    inverse_permutation = get_inverse_permutation(permutation)
    coin_tosses = get_coin_tosses(k)
    for i in range(k):
        if coin_tosses[i] == 0:
            permutation = apply_permutation(permutation, q)
        else:
            permutation = apply_inverse_permutation(permutation, q)
    if permutation == s:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    result = get_result(n, k, q, s)
    print(result)

