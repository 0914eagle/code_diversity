
def get_distinct_modulo_42(numbers):
    distinct_numbers = set()
    for number in numbers:
        distinct_numbers.add(number % 42)
    return len(distinct_numbers)

def main():
    numbers = [int(input()) for _ in range(10)]
    print(get_distinct_modulo_42(numbers))

if __name__ == '__main__':
    main()

