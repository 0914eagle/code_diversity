
def input_numbers(n, m):
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    return numbers

def lossy_sort(numbers, m):
    sorted_numbers = sorted(numbers)
    for i in range(len(sorted_numbers)):
        if sorted_numbers[i] != numbers[i]:
            numbers[i] = sorted_numbers[i]
    return numbers

def main():
    n, m = map(int, input().split())
    numbers = input_numbers(n, m)
    sorted_numbers = lossy_sort(numbers, m)
    for number in sorted_numbers:
        print(number)

if __name__ == '__main__':
    main()

