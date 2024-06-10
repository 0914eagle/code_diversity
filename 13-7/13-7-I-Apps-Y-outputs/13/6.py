
def get_secret_number(n, k):
    # Your code here
    return secret_number

def is_prime(n):
    # Your code here
    return True/False

def is_between(n, a, b):
    # Your code here
    return True/False

def is_even(n):
    # Your code here
    return True/False

def main():
    n, k = map(int, input().split())
    secret_number = get_secret_number(n, k)
    if secret_number % 2 == 0 and is_prime(secret_number):
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")

if __name__ == '__main__':
    main()

