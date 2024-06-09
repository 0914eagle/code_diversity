
def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def get_median_excluding(numbers, excluding):
    numbers.sort()
    if excluding in numbers:
        numbers.remove(excluding)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N):
        print(get_median_excluding(numbers, numbers[i]))

if __name__ == '__main__':
    main()

