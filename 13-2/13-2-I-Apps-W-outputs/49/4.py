
def count_divisible_integers(A):
    # Initialize a set to store the divisible integers
    divisible_integers = set()

    # Iterate over the input array
    for i in range(len(A)):
        # Check if the current element is divisible by any of the previous elements
        for j in range(i):
            if A[i] % A[j] == 0:
                # If it is, add it to the set of divisible integers
                divisible_integers.add(i + 1)
                break

    # Return the length of the set of divisible integers
    return len(divisible_integers)

def main():
    # Read the input data from stdin
    N = int(input())
    A = list(map(int, input().split()))

    # Call the count_divisible_integers function and print the result
    print(count_divisible_integers(A))

if __name__ == '__main__':
    main()

