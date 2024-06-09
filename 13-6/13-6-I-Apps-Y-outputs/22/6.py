
def get_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def get_b_values(numbers):
    b_values = []
    for i in range(len(numbers)):
        numbers_copy = numbers[:i] + numbers[i+1:]
        b_values.append(get_median(numbers_copy))
    return b_values

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    b_values = get_b_values(numbers)
    for b in b_values:
        print(b)

if __name__ == '__main__':
    main()

