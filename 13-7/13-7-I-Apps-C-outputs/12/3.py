
def get_happy_values(n, k, a):
    # Initialize a set to store the happy values
    happy_values = set()
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Get the last digit of the value in the Martian number system
        last_digit = value % k
        
        # If the last digit is divine, add it to the set of happy values
        if last_digit in [0, 4]:
            happy_values.add(last_digit)
    
    return len(happy_values), sorted(list(happy_values))

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_happy_values function
    result = get_happy_values(n, k, a)
    
    # Print the result
    print(result[0])
    print(*result[1])

if __name__ == '__main__':
    main()

