
def get_powers(N):
    powers = []
    for i in range(1, N+1):
        powers.append(int(input()))
    return powers

def get_x(powers):
    x = 0
    for power in powers:
        x += power
    return x

def main():
    N = int(input())
    powers = get_powers(N)
    x = get_x(powers)
    print(x)

if __name__ == '__main__':
    main()

