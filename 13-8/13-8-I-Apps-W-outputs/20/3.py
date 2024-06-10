
def get_kth_digit(k):
    # Initialize a string to store the sequence
    sequence = "1"

    # Iterate through the sequence and add each digit to the string
    for i in range(2, 10**12):
        sequence += str(i)

    # Return the k-th digit of the sequence
    return sequence[k-1]

def main():
    # Read the input k
    k = int(input())

    # Print the k-th digit of the sequence
    print(get_kth_digit(k))

if __name__ == '__main__':
    main()

