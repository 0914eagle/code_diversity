
def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def get_input():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    return numbers

def main():
    numbers = get_input()
    result = multiply(numbers)
    if result > 10**18:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    main()

