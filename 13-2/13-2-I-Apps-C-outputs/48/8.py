
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by the employees
    jokes = set()
    # Add the types of jokes told by Petar to the set
    jokes.add(V[0])
    # Iterate over the direct supervisors of each employee
    for i in range(1, N):
        # If the direct supervisor of the current employee is not invited, skip this employee
        if A[i-1] not in jokes:
            continue
        # If the set of jokes told by the direct supervisor and the current employee don't form a set of consecutive numbers, skip this employee
        if not is_consecutive(jokes, V[i]):
            continue
        # Add the type of joke told by the current employee to the set
        jokes.add(V[i])
    # Return the number of different sets of jokes
    return len(jokes)

def is_consecutive(jokes, joke):
    # If the set of jokes is empty, return True
    if not jokes:
        return True
    # Get the minimum and maximum values in the set of jokes
    min_joke, max_joke = min(jokes), max(jokes)
    # If the difference between the minimum and maximum values is 1 and the current joke is between them, return True
    if max_joke - min_joke == 1 and min_joke < joke < max_joke:
        return True
    # Otherwise, return False
    return False

# Main function
def main():
    # Read the number of employees and their types of jokes from stdin
    N = int(input())
    V = list(map(int, input().split()))
    # Read the direct supervisors of each employee from stdin
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Solve the problem and print the number of different sets of jokes
    print(solve(N, V, A, B))

if __name__ == "__main__":
    main()

