
def f1(n, m, a, b):
    # Calculate the minimum mass of fuel to load into the rocket
    fuel = 0
    for i in range(n):
        fuel += max(a[i], b[i])
    return fuel

def f2(n, m, a, b):
    # Calculate the minimum mass of fuel to load into the rocket, taking into account the weight of the rocket and the payload
    fuel = 0
    for i in range(n):
        fuel += max(a[i], b[i]) + m
    return fuel

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(n, m, a, b))
    print(f2(n, m, a, b))

