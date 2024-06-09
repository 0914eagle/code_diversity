
def get_largest_number(numbers):
    return max(numbers)

def get_unique_elements(numbers):
    unique_elements = set()
    for number in numbers:
        if number not in unique_elements:
            unique_elements.add(number)
    return unique_elements

def get_unique_elements_sorted(numbers):
    return sorted(get_unique_elements(numbers))

def get_sum_of_unique_elements(numbers):
    return sum(get_unique_elements(numbers))

def get_product_of_unique_elements(numbers):
    result = 1
    for element in get_unique_elements(numbers):
        result *= element
    return result

def get_largest_prime_factor(number):
    if number <= 1:
        return number
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

def get_unique_prime_factors(numbers):
    unique_prime_factors = set()
    for number in numbers:
        prime_factors = []
        n = get_largest_prime_factor(number)
        while n > 1:
            prime_factors.append(n)
            n = get_largest_prime_factor(n)
        for prime_factor in prime_factors:
            if prime_factor not in unique_prime_factors:
                unique_prime_factors.add(prime_factor)
    return unique_prime_factors

def get_unique_prime_factors_sorted(numbers):
    return sorted(get_unique_prime_factors(numbers))

def get_sum_of_unique_prime_factors(numbers):
    return sum(get_unique_prime_factors(numbers))

def get_product_of_unique_prime_factors(numbers):
    result = 1
    for element in get_unique_prime_factors(numbers):
        result *= element
    return result

def main():
    numbers = [int(input()) for _ in range(int(input()))]
    print(get_largest_number(numbers))
    print(get_unique_elements_sorted(numbers))
    print(get_sum_of_unique_elements(numbers))
    print(get_product_of_unique_elements(numbers))
    print(get_unique_prime_factors_sorted(numbers))
    print(get_sum_of_unique_prime_factors(numbers))
    print(get_product_of_unique_prime_factors(numbers))

if __name__ == '__main__':
    main()

