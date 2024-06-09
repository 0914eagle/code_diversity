
def get_min_prime(x):
    # Initialize a list to store prime numbers
    prime_list = []
    
    # Iterate from 2 to the given number
    for i in range(2, x + 1):
        # Check if the number is prime
        if is_prime(i):
            # If it is prime, add it to the list
            prime_list.append(i)
    
    # Return the first prime number in the list
    return prime_list[0]

def is_prime(n):
    # Check if the number is divisible by 2 to n-1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    x = int(input())
    print(get_min_prime(x))

