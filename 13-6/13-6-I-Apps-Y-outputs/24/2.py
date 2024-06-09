
def get_powers(n):
    powers = []
    for i in range(1, n+1):
        powers.append(int(input()))
    return powers

def get_x(powers):
    x = 0
    for power in powers:
        x += power
    return x

def main():
    n = int(input())
    powers = get_powers(n)
    x = get_x(powers)
    print(x)

if __name__ == '__main__':
    main()

