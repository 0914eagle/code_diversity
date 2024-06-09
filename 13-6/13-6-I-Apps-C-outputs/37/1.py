
def f1(N, Q):
    # Initialize an empty array of size N
    arr = [0] * (N + 1)
    for i in range(Q):
        # Read the query type and the corresponding values
        query_type, u, v = map(int, input().split())
        if query_type == 1:
            # Update the array by placing a stone in one of the boxes between u and v, inclusive
            arr[u] += 1
            arr[v] += 1
        else:
            # Calculate the expected value of A
            expected_value = 0
            for i in range(1, N + 1):
                expected_value += arr[i] ** 2
            print(expected_value)

def f2(...):
    # Function 2 implementation
    ...

if __name__ == '__main__':
    N, Q = map(int, input().split())
    f1(N, Q)

