
def get_maximum_score(numbers):
    # Calculate the greatest common divisor of all numbers
    gcd = functools.reduce(math.gcd, numbers)
    
    # Calculate the maximum possible score
    maximum_score = sum(numbers) // gcd
    
    # Calculate the smallest number of operations needed to obtain the maximum possible score
    minimum_operations = 0
    for i in range(len(numbers)):
        if numbers[i] % gcd == 0:
            minimum_operations += 1
    
    return maximum_score, minimum_operations

