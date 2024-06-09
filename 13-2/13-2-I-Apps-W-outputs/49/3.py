
def count_divisible_integers(A):
    # Initialize a set to store the divisible integers
    divisible_integers = set()
    # Iterate through the array
    for i in range(len(A)):
        # Check if the current element is divisible by any other element
        for j in range(i+1, len(A)):
            if A[i] % A[j] == 0:
                # If it is divisible, add it to the set
                divisible_integers.add(i+1)
                break
    # Return the length of the set
    return len(divisible_integers)

def main():
    # Read the input
    N = int(input())
    A = list(map(int, input().split()))
    # Call the function to count the divisible integers
    count = count_divisible_integers(A)
    # Print the result
    print(count)

if __name__ == '__main__':
    main()

