def is_multiply_prime(a):
    
    # 1. Check if the number is a multiple of 3
    if a % 3 == 0:
        # 2. Check if the number is a multiple of 5
        if a % 5 == 0:
            # 3. Check if the number is a multiple of 7
            if a % 7 == 0:
                return True
    return False


if __name__ == "__main__":
    print(is_multiply_prime(30))
