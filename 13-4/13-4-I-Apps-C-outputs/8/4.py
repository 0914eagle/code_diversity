
def solve(N, A, B):
    # Initialize a list to store the sequence
    seq = []

    # If A is 0, then the sequence is empty
    if A == 0:
        return seq

    # If B is 0, then the sequence is a single element
    if B == 0:
        return [N]

    # If A is 1, then the sequence is a single increasing element
    if A == 1:
        return [N-B+1]

    # If B is 1, then the sequence is a single decreasing element
    if B == 1:
        return [N-A+1]

    # If A is 2, then the sequence is a pair of increasing elements
    if A == 2:
        return [N-B+1, N-B+2]

    # If B is 2, then the sequence is a pair of decreasing elements
    if B == 2:
        return [N-A+1, N-A+2]

    # If A is 3, then the sequence is a triplet of increasing elements
    if A == 3:
        return [N-B+1, N-B+2, N-B+3]

    # If B is 3, then the sequence is a triplet of decreasing elements
    if B == 3:
        return [N-A+1, N-A+2, N-A+3]

    # If A is greater than 3, then the sequence has at least one increasing element
    if A > 3:
        # Find the largest increasing element in the sequence
        max_inc_element = N-B+1
        for i in range(2, A):
            if max_inc_element < N-B+i:
                max_inc_element = N-B+i

        # Add the largest increasing element to the sequence
        seq.append(max_inc_element)

        # Recursively find the remaining elements of the sequence
        seq += solve(N-1, A-1, B)

        # Return the sequence
        return seq

    # If B is greater than 3, then the sequence has at least one decreasing element
    if B > 3:
        # Find the smallest decreasing element in the sequence
        min_dec_element = N-A+1
        for i in range(2, B):
            if min_dec_element > N-A+i:
                min_dec_element = N-A+i

        # Add the smallest decreasing element to the sequence
        seq.append(min_dec_element)

        # Recursively find the remaining elements of the sequence
        seq += solve(N-1, A, B-1)

        # Return the sequence
        return seq

# Test the function with example inputs
N = 5
A = 3
B = 2
print(solve(N, A, B)) # should print [2, 4, 1, 5, 3]

N = 10
A = 5
B = 4
print(solve(N, A, B)) # should print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10
A = 10
B = 10
print(solve(N, A, B)) # should print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10
A = 5
B = 5
print(solve(N, A, B)) # should print -1

