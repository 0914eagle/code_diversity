
def is_divisible_by_3(n):
    return n % 3 == 0

def is_divisible_by_5(n):
    return n % 5 == 0

def is_divisible_by_3_and_5(n):
    return is_divisible_by_3(n) and is_divisible_by_5(n)

def get_fizz_buzz_sequence(n):
    sequence = []
    for i in range(1, n+1):
        if is_divisible_by_3_and_5(i):
            sequence.append("FizzBuzz")
        elif is_divisible_by_3(i):
            sequence.append("Fizz")
        elif is_divisible_by_5(i):
            sequence.append("Buzz")
        else:
            sequence.append(i)
    return sequence

def get_sum_of_numbers(sequence):
    return sum(int(x) for x in sequence if x.isdigit())

if __name__ == '__main__':
    n = int(input())
    sequence = get_fizz_buzz_sequence(n)
    print(get_sum_of_numbers(sequence))

