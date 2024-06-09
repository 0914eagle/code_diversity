
def get_digits_needed(n):
    return len(str(n))

def get_number_of_distinct_numbers(n):
    return n

def get_number_of_digits_needed(n):
    distinct_numbers = get_number_of_distinct_numbers(n)
    digits_needed = get_digits_needed(distinct_numbers)
    return digits_needed

if __name__ == '__main__':
    n = int(input())
    print(get_number_of_digits_needed(n))

