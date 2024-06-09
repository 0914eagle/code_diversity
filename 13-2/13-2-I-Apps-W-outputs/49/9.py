
def count_divisible_numbers(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] % numbers[j] == 0:
                count += 1
    return count

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(count_divisible_numbers(numbers))

if __name__ == '__main__':
    main()

