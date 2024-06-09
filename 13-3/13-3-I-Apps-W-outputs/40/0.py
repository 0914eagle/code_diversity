
def get_max_score(numbers):
    # Calculate the greatest common divisor of all numbers
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = gcd(numbers[i], gcd)
    
    # Calculate the smallest number of operations needed to obtain the maximum score
    operations = 0
    while gcd > 1:
        for i in range(len(numbers)):
            if numbers[i] % gcd == 0:
                numbers[i] //= gcd
                break
        gcd -= 1
        operations += 1
    
    return gcd, operations

