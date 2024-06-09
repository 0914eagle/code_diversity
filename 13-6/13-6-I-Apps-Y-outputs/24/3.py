
def get_powers(powers):
    powers_dict = {}
    for power in powers:
        num, pow = str(power)
        if num not in powers_dict:
            powers_dict[num] = [int(pow)]
        else:
            powers_dict[num].append(int(pow))
    return powers_dict

def get_x(numbers, powers):
    x = 0
    for num, pow in powers.items():
        x += int(num) ** sum(pow)
    return x

def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    powers = get_powers(numbers)
    x = get_x(numbers, powers)
    print(x)

if __name__ == '__main__':
    main()

