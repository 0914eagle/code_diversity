
def f1(n, S):
    # find the largest non-negative integer x such that there is a magical permutation of integers from 0 to 2^x - 1
    x = 0
    while True:
        if is_magical_permutation(x, S):
            return x
        x += 1

def is_magical_permutation(x, S):
    # check if the permutation of integers from 0 to 2^x - 1 is magical
    permutation = list(range(2**x))
    for i in range(2**x - 1):
        if permutation[i] ^ permutation[i+1] not in S:
            return False
    return True

def f2(n, S):
    # find a magical permutation of integers from 0 to 2^x - 1
    x = f1(n, S)
    permutation = list(range(2**x))
    return permutation

if __name__ == '__main__':
    n = int(input())
    S = set(map(int, input().split()))
    x = f1(n, S)
    print(x)
    permutation = f2(n, S)
    print(*permutation)

