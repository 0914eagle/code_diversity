
def solve(A, B):
    # Calculate the number of appearances of numbers from the interval [A, B]
    count = 0
    for i in range(A, B+1):
        count += 1
    return count

def main():
    # Read the number of queries
    Q = int(input())

    # Iterate over each query
    for i in range(Q):
        # Read the query
        A, B = map(int, input().split())

        # Calculate the answer
        answer = solve(A, B)

        # Print the answer
        print(answer)

if __name__ == '__main__':
    main()

