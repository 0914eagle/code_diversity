
def get_happy_digits(n, k, a):
    # Initialize a set to store the happy digits
    happy_digits = set()
    
    # Loop through each denomination and calculate the last digit in the octal system
    for i in range(n):
        last_digit = str(oct(a[i])).split("o")[1][-1]
        if last_digit in ["0", "4"]:
            happy_digits.add(last_digit)
    
    # Return the number of happy digits and the set of happy digits
    return len(happy_digits), happy_digits

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_happy_digits function and print the output
    num_happy_digits, happy_digits = get_happy_digits(n, k, a)
    print(num_happy_digits)
    print(*happy_digits, sep=" ")

if __name__ == '__main__':
    main()

