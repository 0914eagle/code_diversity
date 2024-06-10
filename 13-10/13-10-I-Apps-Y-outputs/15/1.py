
def get_x(powers, numbers):
    x = 0
    for i in range(len(numbers)):
        x += numbers[i] ** int(powers[i])
    return x

def main():
    n = int(input())
    powers = input().split()
    numbers = [int(input()) for _ in range(n)]
    print(get_x(powers, numbers))

if __name__ == '__main__':
    main()

