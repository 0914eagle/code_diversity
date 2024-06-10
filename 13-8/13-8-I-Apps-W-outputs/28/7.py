
def get_steps(a, b):
    # find the smallest number that is a multiple of both a and b
    lcm = a * b // gcd(a, b)
    # find the interval of steps that covers the lcm
    l, r = 1, lcm // a
    return l, r

def check_interval(a, b, l, r):
    # check if the interval of steps from l to r has the correct number of even and odd steps
    even_steps = 0
    odd_steps = 0
    for i in range(l, r + 1):
        if i % 2 == 0:
            even_steps += 1
        else:
            odd_steps += 1
    return even_steps == a and odd_steps == b

def main():
    a, b = map(int, input().split())
    l, r = get_steps(a, b)
    if check_interval(a, b, l, r):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

