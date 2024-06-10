
def get_lcm(n):
    lcm = 1
    for i in range(1, n + 1):
        if n % i == 0:
            lcm *= i
    return lcm

def get_max_lcm(n):
    lcm1 = get_lcm(n)
    lcm2 = get_lcm(n - 1)
    lcm3 = get_lcm(n - 2)
    return max(lcm1, lcm2, lcm3)

if __name__ == '__main__':
    n = int(input())
    print(get_max_lcm(n))

