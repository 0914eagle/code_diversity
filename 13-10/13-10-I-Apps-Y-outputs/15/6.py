
def calculate_x(powers, numbers):
    x = 0
    for i in range(len(numbers)):
        x += numbers[i] ** powers[i]
    return x

def main():
    n = int(input())
    powers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    print(calculate_x(powers, numbers))

if __name__ == '__main__':
    main()

