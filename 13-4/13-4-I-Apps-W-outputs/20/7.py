
def find_permutation(n):
    # Initialize a list to store the permutation
    permutation = [0] * n

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Find the index of the element that is not equal to its index
        index = (i + 1) % n

        # If the element at the index is not equal to its index,
        # then we have found the next element of the permutation
        if permutation[index - 1] != index:
            permutation[i - 1] = index
        # Otherwise, we need to find the next available element
        else:
            # Iterate from the index to n
            for j in range(index, n):
                # If the element at the index is not equal to its index,
                # then we have found the next element of the permutation
                if permutation[j - 1] != j:
                    permutation[i - 1] = j
                    break

    # Return the permutation
    return permutation

def find_permutation_bitwise(n):
    # Initialize a list to store the permutation
    permutation = [0] * n

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Find the index of the element that is not equal to its index
        index = (i + 1) % n

        # If the element at the index is not equal to its index,
        # then we have found the next element of the permutation
        if permutation[index - 1] != index:
            permutation[i - 1] = index
        # Otherwise, we need to find the next available element
        else:
            # Iterate from the index to n
            for j in range(index, n):
                # If the element at the index is not equal to its index,
                # then we have found the next element of the permutation
                if permutation[j - 1] != j:
                    permutation[i - 1] = j
                    break

    # Return the permutation
    return permutation

n = int(input())
permutation = find_permutation(n)
print("YES")
print(" ".join(str(x) for x in permutation))
permutation = find_permutation_bitwise(n)
print("YES")
print(" ".join(str(x) for x in permutation))

