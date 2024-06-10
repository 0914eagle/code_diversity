
def get_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    while b:
        a, b = b, a % b
    return a

def get_max_lcm(n):
    lcm = 1
    for i in range(2, n + 1):
        lcm = get_lcm(lcm, i)
    return lcm

def main():
    n = int(input())
    print(get_max_lcm(n))

if __name__ == '__main__':
    main()

