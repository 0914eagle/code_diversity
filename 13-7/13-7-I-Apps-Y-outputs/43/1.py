
def solve(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the guessed numbers to be the first three numbers
    a, b, c = numbers[:3]
    # Calculate the sum of the guessed numbers
    sum_abc = a + b + c
    # Calculate the pairwise sums of the guessed numbers
    ab = a + b
    ac = a + c
    bc = b + c
    # Check if the pairwise sums and the sum of the guessed numbers match the given numbers
    if ab == numbers[3] and ac == numbers[2] and bc == numbers[1]:
        return [a, b, c]
    # If the numbers do not match, try all possible permutations of the guessed numbers
    for i in range(3):
        for j in range(i+1, 3):
            for k in range(j+1, 3):
                a, b, c = numbers[i], numbers[j], numbers[k]
                if ab == numbers[3] and ac == numbers[2] and bc == numbers[1]:
                    return [a, b, c]
    # If no permutation works, return an empty list to indicate failure
    return []

