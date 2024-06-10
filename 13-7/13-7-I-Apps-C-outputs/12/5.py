
def get_happy_numbers(n, k, a):
    # Initialize an empty list to store the happy numbers
    happy_numbers = []
    
    # Iterate over the given denominations
    for i in range(n):
        # Calculate the value of the current denomination in the Martian number system
        value = int(str(a[i])[::-1], k)
        
        # Check if the last digit of the value is a divine digit
        if str(value)[-1] in "40":
            # Add the current denomination to the list of happy numbers
            happy_numbers.append(a[i])
    
    return happy_numbers

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_happy_numbers function
    happy_numbers = get_happy_numbers(n, k, a)
    
    # Print the number of happy numbers
    print(len(happy_numbers))
    
    # Print the happy numbers in increasing order
    for happy_number in sorted(happy_numbers):
        print(happy_number)

if __name__ == '__main__':
    main()

