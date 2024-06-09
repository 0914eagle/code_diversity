
def solve(a, k):
    n = len(a)
    x = 0
    moves = 0
    while True:
        # find the smallest number that is not divisible by k
        not_divisible = [i for i in range(n) if a[i] % k != 0]
        if not not_divisible:
            break
        # increase x by 1
        x += 1
        # add x to the elements that are not divisible by k
        for i in not_divisible:
            a[i] += x
        moves += 1
    return moves

