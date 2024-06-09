
def get_largest_sum(A, K):
    # Calculate the original sum of the array
    original_sum = sum(A)

    # Sort the array in descending order
    A.sort(reverse=True)

    # Initialize the largest sum
    largest_sum = 0

    # Loop through each element in the array
    for i in range(len(A)):
        # Calculate the sum of the array after modifying the current element
        current_sum = sum(A[:i] + A[i+1:])

        # If the sum is larger than the largest sum, update the largest sum
        if current_sum > largest_sum:
            largest_sum = current_sum

    # Return the largest sum
    return largest_sum

def main():
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum(A, K))

if __name__ == '__main__':
    main()

