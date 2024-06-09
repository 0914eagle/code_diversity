
def sift_greek_numbers(n):
    # Initialize an empty list to store the sifted numbers
    sifted_numbers = []
    
    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Check if the number is divisible by 2, 3, or 5
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            # If it is, add it to the list of sifted numbers
            sifted_numbers.append(i)
    
    # Return the sum of the sifted numbers
    return sum(sifted_numbers)

def main():
    n = int(input())
    print(sift_greek_numbers(n))

if __name__ == '__main__':
    main()

