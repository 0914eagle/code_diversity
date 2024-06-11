def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, a):
            if a % i == 0:
                for j in range(2, i):
                    if i % j == 0:
                        return False
                return True
    return False


if __name__ == '__main__':
    print(is_multiply_prime(30))
