
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by the invited guests
    invited_jokes = set()

    # Iterate through the list of direct supervisors
    for i in range(len(A)):
        # If the direct supervisor of the current guest is not invited, do not invite the current guest
        if A[i] not in invited_jokes:
            continue

        # If the set of jokes told by the current guest and their direct supervisor do not form a set of consecutive numbers, do not invite the current guest
        if not is_consecutive(V[i], V[A[i] - 1]):
            continue

        # If the current guest is already invited, do not invite them again
        if V[i] in invited_jokes:
            continue

        # If all conditions are met, invite the current guest and add their type of joke to the set
        invited_jokes.add(V[i])

    # Return the number of different sets of jokes
    return len(invited_jokes)

def is_consecutive(a, b):
    # Sort the two numbers in ascending order
    a, b = sorted([a, b])

    # Check if the difference between the two numbers is exactly 1
    return a + 1 == b

# Main function
if __name__ == '__main__':
    # Read the input
    N = int(input())
    V = list(map(int, input().split()))
    A = []
    B = []
    for i in range(N - 1):
        A.append(int(input()))
        B.append(int(input()))

    # Solve the problem
    print(solve(N, V, A, B))

