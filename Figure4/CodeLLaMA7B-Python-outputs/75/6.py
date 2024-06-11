def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, a):
            if a % i == 0:
                for j in range(2, i):
                    if i % j == 0:
                        return False
        return True
    else:
        return False


print(is_multiply_prime(30))
print(is_multiply_prime(12))
print(is_multiply_prime(11))
print(is_multiply_prime(10))
print(is_multiply_prime(9))
print(is_multiply_prime(8))
print(is_multiply_prime(7))
print(is_multiply_prime(6))
print(is_multiply_prime(5))
print(is_multiply_prime(4))
print(is_multiply_prime(3))
print(is_multiply_prime(2))
print(is_multiply_prime(1))
