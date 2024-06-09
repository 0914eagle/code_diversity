
def get_lcm(arr):
    lcm = 1
    for i in range(len(arr)):
        lcm = lcm * arr[i] // gcd(lcm, arr[i])
    return lcm

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(arr):
    lcm = get_lcm(arr)
    for i in range(len(arr)):
        if lcm % arr[i] != 0:
            return -1
    return lcm

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

