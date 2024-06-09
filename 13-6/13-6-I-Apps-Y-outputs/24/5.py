
def get_power(pow_str):
    return int(pow_str)

def get_number(num_str):
    return int(num_str)

def get_x(powers, numbers):
    x = 0
    for i in range(len(powers)):
        x += numbers[i] ** get_power(powers[i])
    return x

def main():
    n = int(input())
    powers = [input() for _ in range(n)]
    numbers = [input() for _ in range(n)]
    print(get_x(powers, numbers))

if __name__ == '__main__':
    main()

