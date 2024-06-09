
def is_divisible_by_3(n):
    return n % 3 == 0

def is_divisible_by_5(n):
    return n % 5 == 0

def get_fizz_buzz(n):
    if is_divisible_by_3(n) and is_divisible_by_5(n):
        return "FizzBuzz"
    elif is_divisible_by_3(n):
        return "Fizz"
    elif is_divisible_by_5(n):
        return "Buzz"
    else:
        return str(n)

def get_sum_of_first_n_terms(n):
    sum = 0
    for i in range(1, n+1):
        term = get_fizz_buzz(i)
        if term != "Fizz" and term != "Buzz":
            sum += int(term)
    return sum

if __name__ == '__main__':
    n = int(input())
    print(get_sum_of_first_n_terms(n))

