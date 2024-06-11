def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, 100):
            if a % i == 0:
                for j in range(2, 100):
                    if i % j == 0:
                        for k in range(2, 100):
                            if j % k == 0:
                                return True
        return False
    else:
        return "Error: the number is greater than 100"


print(is_multiply_prime(30))
print(is_multiply_prime(100))
