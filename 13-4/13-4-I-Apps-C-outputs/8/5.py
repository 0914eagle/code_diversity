
def solve(N, A, B):
    # Initialize a list to store the sequence
    seq = []

    # If A is 1, we can simply create a sequence of length N with elements from 1 to N
    if A == 1:
        return list(range(1, N+1))

    # If B is 1, we can create a sequence of length N with elements from N to 1
    if B == 1:
        return list(range(N, 0, -1))

    # If A is greater than N or B is greater than N, there is no valid sequence
    if A > N or B > N:
        return -1

    # If A is equal to B, we can create a sequence of length N with elements from 1 to N in alternating order
    if A == B:
        return [i if i % 2 == 0 else N-i+1 for i in range(1, N+1)]

    # If A is greater than B, we can create a sequence of length N with elements from 1 to N in increasing order,
    # and then reverse the elements from 1 to B to create a decreasing subsequence
    if A > B:
        seq = list(range(1, N+1))
        return seq[:B] + seq[B:A][::-1] + seq[A:]

    # If B is greater than A, we can create a sequence of length N with elements from N to 1 in decreasing order,
    # and then reverse the elements from N-A+1 to N to create an increasing subsequence
    if B > A:
        seq = list(range(N, 0, -1))
        return seq[:A] + seq[A:B][::-1] + seq[B:]

# Test the function with example input
N = 5
A = 3
B = 2
print(solve(N, A, B))

# Test the function with another example input
N = 10
A = 5
B = 3
print(solve(N, A, B))

