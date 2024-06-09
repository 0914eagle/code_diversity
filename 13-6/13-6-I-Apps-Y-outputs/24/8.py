
def get_powers(powers):
    powers = [int(power) for power in powers]
    return powers

def get_numbers(numbers):
    numbers = [int(number) for number in numbers]
    return numbers

def get_x(numbers, powers):
    x = 0
    for i in range(len(numbers)):
        x += numbers[i] ** powers[i]
    return x

def main():
    n = int(input())
    numbers = get_numbers(input().split())
    powers = get_powers(input().split())
    x = get_x(numbers, powers)
    print(x)

if __name__ == '__main__':
    main()

