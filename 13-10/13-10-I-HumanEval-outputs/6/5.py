
def is_multiply_prime(a: int) -> bool:
    
    if a < 100:
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(len(prime_numbers)):
            for j in range(i+1, len(prime_numbers)):
                for k in range(j+1, len(prime_numbers)):
                    if a == prime_numbers[i] * prime_numbers[j] * prime_numbers[k]:
                        return True
    return False

