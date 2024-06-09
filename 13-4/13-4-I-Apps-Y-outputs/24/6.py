
def get_fizzbuzz_sequence(n):
    sequence = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            sequence.append("FizzBuzz")
        elif i % 3 == 0:
            sequence.append("Fizz")
        elif i % 5 == 0:
            sequence.append("Buzz")
        else:
            sequence.append(i)
    return sequence

def get_sum_of_numbers(sequence):
    sum = 0
    for i in sequence:
        if isinstance(i, int):
            sum += i
    return sum

if __name__ == '__main__':
    n = int(input())
    sequence = get_fizzbuzz_sequence(n)
    print(get_sum_of_numbers(sequence))

