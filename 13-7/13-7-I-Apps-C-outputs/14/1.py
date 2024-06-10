
def get_lcm(n):
    lcm = 1
    for i in range(2, n+1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def get_max_lcm_of_three(n):
    lcm1 = get_lcm(n)
    lcm2 = get_lcm(n-1)
    lcm3 = get_lcm(n-2)
    return max(lcm1, lcm2, lcm3)

if __name__ == '__main__':
    n = int(input())
    print(get_max_lcm_of_three(n))

