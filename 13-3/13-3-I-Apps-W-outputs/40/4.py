
def get_maximum_score(numbers):
    # Calculate the greatest common divisor of all numbers
    gcd = get_gcd(numbers)
    
    # Calculate the maximum possible score
    score = sum(numbers) // gcd
    
    # Calculate the smallest number of operations needed to obtain the maximum possible score
    operations = 0
    for num in numbers:
        if num % gcd != 0:
            operations += 1
    
    return score, operations

def get_gcd(numbers):
    if len(numbers) == 2:
        return get_gcd_two_numbers(numbers[0], numbers[1])
    else:
        return get_gcd(numbers[1:])

def get_gcd_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return get_gcd_two_numbers(b, a % b)

numbers = [int(x) for x in input().split()]
score, operations = get_maximum_score(numbers)
print(score, operations)

