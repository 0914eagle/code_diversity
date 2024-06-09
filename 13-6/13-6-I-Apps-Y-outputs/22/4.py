
def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def get_median_excluding_i(numbers, i):
    numbers.sort()
    return get_median(numbers[:i] + numbers[i+1:])

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    for i in range(1, n+1):
        print(get_median_excluding_i(numbers, i-1))

if __name__ == '__main__':
    main()

