
def find_divisible_number(numbers):
    for i in range(1, max(numbers) + 1):
        if all(number % i == 0 for number in numbers):
            return i
    return -1

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_divisible_number(numbers))

if __name__ == '__main__':
    main()

