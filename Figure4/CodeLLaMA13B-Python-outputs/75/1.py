def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_multiply_prime(30))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(15) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(91) == True
    assert is_multiply_prime(100) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
