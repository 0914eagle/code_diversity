def is_multiply_prime(a):
    
    prime_list = []
    for i in range(2, a):
        if a % i == 0:
            prime_list.append(i)
    if len(prime_list) == 3:
        return True
    else:
        return False


print(is_multiply_prime(30))
