
def get_powers(n):
    powers = []
    for i in range(n):
        powers.append(int(input()))
    return powers

def get_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    return numbers

def solve(numbers, powers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i] ** powers[i]
    return result

def main():
    n = int(input())
    numbers = get_numbers(n)
    powers = get_powers(n)
    print(solve(numbers, powers))

if __name__ == '__main__':
    main()

