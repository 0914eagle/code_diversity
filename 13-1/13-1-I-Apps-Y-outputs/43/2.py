
def get_min_prime(x):
    # Initialize a list to store prime numbers
    prime_list = []
    
    # Iterate from 2 to the square root of x
    for i in range(2, int(x**0.5) + 1):
        # Check if i is prime
        if is_prime(i):
            # Add i to the list of prime numbers
            prime_list.append(i)
    
    # Return the first prime number greater than or equal to x
    for prime in prime_list:
        if prime >= x:
            return prime
    
    # If no prime number is greater than or equal to x, return -1
    return -1

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    x = int(input())
    print(get_min_prime(x))

