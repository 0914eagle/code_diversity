
def get_largest_sum(A, K):
    # Calculate the original sum of the array
    original_sum = sum(A)

    # Sort the array in descending order
    A.sort(reverse=True)

    # Initialize a variable to keep track of the number of elements that have been modified
    num_modified = 0

    # Loop through the array and modify the elements
    for i in range(len(A)):
        # If the number of modifications is less than K, modify the current element and increment the number of modifications
        if num_modified < K:
            A[i] = -A[i]
            num_modified += 1
        # If the number of modifications is equal to K, break out of the loop
        elif num_modified == K:
            break

    # Calculate the modified sum of the array
    modified_sum = sum(A)

    # Return the largest possible sum, which is the maximum of the original sum and the modified sum
    return max(original_sum, modified_sum)

def main():
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum(A, K))

    A = [3, -1, 0, 2]
    K = 3
    print(get_largest_sum(A, K))

    A = [2, -3, -1, 5, -4]
    K = 2
    print(get_largest_sum(A, K))

if __name__ == '__main__':
    main()

