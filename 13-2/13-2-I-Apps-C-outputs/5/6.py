
def f1(n, r, m):
    # Initialize variables
    tricks = []
    total_time = 0
    expected_time = 0

    # Loop through each trick
    for i in range(m):
        t, p, d = map(int, input().split())
        tricks.append((t, p, d))
        total_time += t

    # Loop through each possible number of attempts
    for i in range(1, r):
        # Calculate the probability of success for each attempt
        prob_success = 1
        for t, p, d in tricks:
            prob_success *= (1 - (1 - p) ** i)

        # Calculate the expected time for each attempt
        expected_time += prob_success * (total_time - i * d)

    # Return the minimum expected time
    return expected_time

def f2(...):
    # Your code here
    return ...

if __name__ == '__main__':
    n = int(input())
    r = int(input())
    m = int(input())
    print(f1(n, r, m))

