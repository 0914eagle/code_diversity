
def get_lcm(a, b):
    # find the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    # return the least common multiple as the product of a and b divided by their gcd
    return a * b // gcd

def _get_gcd(a, b):
    if b == 0:
        return a
    else:
        return _get_gcd(b, a % b)

def solve(arr):
    # find the pair of indices with the minimum lcm
    min_lcm = float('inf')
    min_indices = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            lcm = get_lcm(arr[i], arr[j])
            if lcm < min_lcm:
                min_lcm = lcm
                min_indices = [i, j]
    return min_indices

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*solve(arr))

