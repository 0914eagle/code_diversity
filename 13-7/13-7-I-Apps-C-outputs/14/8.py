
def find_lcm(n):
    lcm = 1
    for i in range(1, n+1):
        if n % i == 0:
            lcm *= i
    return lcm

def find_maximum_lcm(n):
    lcm1 = find_lcm(n)
    lcm2 = find_lcm(n-1)
    lcm3 = find_lcm(n-2)
    return max(lcm1, lcm2, lcm3)

if __name__ == '__main__':
    n = int(input())
    print(find_maximum_lcm(n))

