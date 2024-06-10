
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    while b > 0:
        a, b = b, a % b
    return a

def solve(a):
    n = len(a)
    max_lcm = 0
    for i in range(n):
        for j in range(i+1, n):
            lcm_value = lcm(a[i], a[j])
            if lcm_value > max_lcm:
                max_lcm = lcm_value
    return max_lcm

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

if __name__ == '__main__':
    main()

